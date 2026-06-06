(function () {
  const REFRESH_INTERVAL_MS = 30000;
  const FILE_PROTOCOL = window.location.protocol === "file:";

  const interventionReasonText = {
    blocked: "Blocked by an upstream dependency or gate.",
    "stale-state": "State has not moved for several days.",
    "missing-owner": "Owner role is missing or unclear.",
    "missing-approval": "Required review or approval is still outstanding.",
    "failed-validation": "Validation evidence is failing or incomplete.",
    "missing-traceability": "Traceability row is incomplete or missing.",
    "sync-missing": "Jira or Confluence reference is missing from traceability.",
  };

  const interventionActionText = {
    blocked: "Escalate the blocker, confirm ownership, and re-check the next gate before asking for more work.",
    "stale-state": "Confirm the status with the owner and move the item forward or close out the inactive path.",
    "missing-owner": "Assign the correct owner role so the work has a clear decision path.",
    "missing-approval": "Request the next approval gate and make the review path explicit.",
    "failed-validation": "Review the failing validation evidence and rerun the required checks.",
    "missing-traceability": "Update the traceability matrix so the feature can be governed end to end.",
    "sync-missing": "Add the Jira or Confluence reference to restore synchronization with the source-of-truth chain.",
  };

  const interventionPriority = [
    "blocked",
    "failed-validation",
    "missing-traceability",
    "sync-missing",
    "missing-owner",
    "missing-approval",
    "stale-state",
  ];

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  function normalize(value) {
    return String(value ?? "").toLowerCase().replace(/[^a-z0-9]+/g, "");
  }

  function badgeClass(value) {
    const text = String(value ?? "").toLowerCase();
    if (!text) return "badge chip-muted";
    if (text.includes("pass") || text.includes("ready") || text.includes("complete") || text.includes("approved")) {
      return "badge badge-ok";
    }
    if (text.includes("block") || text.includes("fail") || text.includes("missing") || text.includes("reject")) {
      return "badge badge-danger";
    }
    if (text.includes("draft") || text.includes("review") || text.includes("pending") || text.includes("warn") || text.includes("partial")) {
      return "badge badge-warn";
    }
    return "badge badge-info";
  }

  function asChip(value, kind) {
    const cls = kind ? `chip ${kind}` : "chip";
    return `<span class="${cls}">${escapeHtml(value)}</span>`;
  }

  function formatCount(value) {
    return Number.isFinite(value) ? value.toLocaleString() : String(value ?? 0);
  }

  function formatTimestamp(value) {
    if (!value) return "Unknown";
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? String(value) : date.toLocaleString();
  }

  function artifactHref(path) {
    if (!path) return "";
    return `../${path}`;
  }

  function renderSummary(summary) {
    const items = [
      ["Total features", summary.totalFeatures, "Features discovered across domains"],
      ["Blocked features", summary.blockedFeatures, "Features flagged as blocked"],
      ["Validation passed", summary.validationPassed, "Features with explicit passing validation"],
      ["Validation failed", summary.validationFailed, "Features with failing or incomplete validation"],
      ["Traceability coverage", `${summary.traceabilityCoveragePercent}%`, "Features linked to traceability rows"],
      ["Release-ready", summary.releaseReadyFeatures, "Features marked ready for release"],
    ];

    return items
      .map(
        ([label, value, sub]) => `
          <article class="metric">
            <div class="label">${escapeHtml(label)}</div>
            <div class="value">${escapeHtml(formatCount(value))}</div>
            <div class="sub">${escapeHtml(sub)}</div>
          </article>`
      )
      .join("");
  }

  function renderStateChips(featuresByState) {
    return Object.entries(featuresByState || {})
      .map(([state, count]) => asChip(`${state}: ${count}`, "chip-muted"))
      .join("");
  }

  function workflow(feature) {
    return feature?.workflow || {};
  }

  function featureState(feature) {
    const wf = workflow(feature);
    return wf.state || feature?.state || "";
  }

  function featureOwnerRole(feature) {
    const wf = workflow(feature);
    return wf.owner_role || feature?.ownerRole || "";
  }

  function featureNextGate(feature) {
    const wf = workflow(feature);
    return wf.next_gate || feature?.nextGate || "";
  }

  function featureBlockedReason(feature) {
    const wf = workflow(feature);
    return wf.blocked_reason || feature?.blockedReason || "";
  }

  function featureDaysInState(feature) {
    const wf = workflow(feature);
    const value = wf.days_in_state;
    if (Number.isFinite(value)) return value;
    return Number.isFinite(feature?.daysInState) ? feature.daysInState : 0;
  }

  function featureLastUpdated(feature) {
    const wf = workflow(feature);
    return wf.last_updated || feature?.lastUpdated || feature?.updatedAt || feature?.evidence?.updatedAt || "";
  }

  function featureApproverRole(feature) {
    const wf = workflow(feature);
    return wf.approver_role ?? null;
  }

  function parseTimestamp(value) {
    if (!value) return null;
    const parsed = new Date(value);
    return Number.isNaN(parsed.getTime()) ? null : parsed;
  }

  function selectFeaturedFeature(features) {
    const blocked = features.find((feature) => feature.blocked);
    if (blocked) return blocked;

    const failedValidation = features.find((feature) => {
      const status = normalize(feature.quality?.validationStatus);
      return status.includes("fail") || status.includes("blocked") || status.includes("notready") || status.includes("partial");
    });
    if (failedValidation) return failedValidation;

    const withTimestamp = features
      .map((feature) => ({
        feature,
        timestamp: parseTimestamp(featureLastUpdated(feature)) || null,
      }))
      .filter((entry) => entry.timestamp)
      .sort((left, right) => right.timestamp - left.timestamp);
    if (withTimestamp.length) return withTimestamp[0].feature;

    return features[0] || null;
  }

  function renderFeatureLink(label, path) {
    if (!path) return null;
    return `<a href="${escapeHtml(artifactHref(path))}" target="_blank" rel="noreferrer">${escapeHtml(label)}</a>`;
  }

  function renderFeaturedFeature(feature) {
    if (!feature) {
      return '<div class="empty-state">No feature data is available yet.</div>';
    }

    const pathLinks = [
      renderFeatureLink("Intent", feature.paths?.intent),
      renderFeatureLink("Spec", feature.paths?.specification),
      renderFeatureLink("Design", feature.paths?.design),
      renderFeatureLink("Tests", feature.paths?.tests),
    ].filter(Boolean);

    return `
      <article class="featured-card">
        <div class="header">
          <div>
            <div class="feature">${escapeHtml(feature.feature)}</div>
            <div class="meta">${escapeHtml(feature.domain)} / ${escapeHtml(feature.capability)}</div>
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:flex-end">
            <span class="${badgeClass(featureState(feature))}">${escapeHtml(featureState(feature))}</span>
            ${feature.focus ? `<span class="badge badge-info">Focus</span>` : ""}
          </div>
        </div>
        <div class="featured-grid">
          <div class="featured-tile">
            <div class="label">Owner role</div>
            <div class="value">${escapeHtml(featureOwnerRole(feature) || "Missing owner")}</div>
          </div>
          <div class="featured-tile">
            <div class="label">Next gate</div>
            <div class="value">${escapeHtml(featureNextGate(feature) || "Missing")}</div>
          </div>
          <div class="featured-tile">
            <div class="label">Jira / Confluence</div>
            <div class="value">${escapeHtml(feature.jiraKey || "Missing")} / ${escapeHtml(feature.confluencePageId || "Missing")}</div>
          </div>
          <div class="featured-tile">
            <div class="label">Traceability</div>
            <div class="value">${escapeHtml(feature.traceabilityId || "Missing")}</div>
          </div>
          <div class="featured-tile">
            <div class="label">Approver role</div>
            <div class="value">${escapeHtml(featureApproverRole(feature) || "Unavailable")}</div>
          </div>
          <div class="featured-tile">
            <div class="label">Last updated</div>
            <div class="value">${escapeHtml(formatTimestamp(featureLastUpdated(feature)))}</div>
          </div>
        </div>
        <div class="chip-row" style="margin-top:0">
          ${pathLinks.map((item) => `<span class="chip chip-muted">${item}</span>`).join("")}
        </div>
      </article>`;
  }

  function pipelineRow(feature) {
    const focusTag = feature.focus ? `<span class="pill badge-info">Demo focus</span>` : "";
    const blockedTag = feature.blocked ? `<span class="badge badge-danger">Yes</span>` : `<span class="badge badge-ok">No</span>`;
    const jira = feature.jiraKey
      ? `<a href="${escapeHtml(feature.links.jiraUrl || "#")}" target="_blank" rel="noreferrer">${escapeHtml(feature.jiraKey)}</a>`
      : '<span class="small">Missing</span>';
    const confluence = feature.confluencePageId
      ? `<a href="${escapeHtml(feature.links.confluenceUrl || "#")}" target="_blank" rel="noreferrer">${escapeHtml(feature.confluencePageId)}</a>`
      : '<span class="small">Missing</span>';

    return `
      <tr class="${feature.focus ? "focus-row" : ""}">
        <td>${escapeHtml(feature.domain)}${focusTag ? `<div style="margin-top:6px">${focusTag}</div>` : ""}</td>
        <td>${escapeHtml(feature.capability)}</td>
        <td>
          <div><strong>${escapeHtml(feature.feature)}</strong></div>
          <div class="small">${escapeHtml(feature.featureId)}</div>
        </td>
        <td><span class="${badgeClass(featureState(feature))}">${escapeHtml(featureState(feature))}</span></td>
        <td>${escapeHtml(featureOwnerRole(feature) || "Missing")}</td>
        <td>${escapeHtml(featureDaysInState(feature))}</td>
        <td>${blockedTag}</td>
        <td>${escapeHtml(featureNextGate(feature) || "Missing")}</td>
        <td>${jira}</td>
        <td>${confluence}</td>
      </tr>`;
  }

  function renderPipeline(features) {
    const header = `
      <thead>
        <tr>
          <th>Domain</th>
          <th>Capability</th>
          <th>Feature</th>
          <th>Current State</th>
          <th>Owner Role</th>
          <th>Days in State</th>
          <th>Blocked?</th>
          <th>Next Gate</th>
          <th>Jira Key</th>
          <th>Confluence Page</th>
        </tr>
      </thead>`;
    return header + `<tbody>${features.map(pipelineRow).join("")}</tbody>`;
  }

  function renderApprovalQueue(queue) {
    const entries = [
      ["PO / BA review", queue["PO / BA review"]],
      ["QA review", queue["QA review"]],
      ["SA review", queue["SA review"]],
      ["Dev review", queue["Dev review"]],
      ["DevOps / release review", queue["DevOps / release review"]],
    ];
    return entries
      .map(
        ([label, count]) => `
          <article class="queue-card">
            <div class="label">${escapeHtml(label)}</div>
            <div class="queue-count">${escapeHtml(formatCount(count))}</div>
            <div class="queue-note">Features waiting for this gate</div>
          </article>`
      )
      .join("");
  }

  function renderSquadView(features) {
    const squads = new Map();

    for (const feature of features) {
      const squad = featureOwnerRole(feature) || "Missing owner";
      const entry = squads.get(squad) || {
        squad,
        featuresOwned: 0,
        blockedCount: 0,
        inReviewCount: 0,
        inDevelopmentCount: 0,
        validationFailedCount: 0,
      };

      entry.featuresOwned += 1;
      if (feature.blocked) {
        entry.blockedCount += 1;
      }

      const state = normalize(featureState(feature));
      const nextGate = normalize(featureNextGate(feature));
      if (state.includes("draft") || state.includes("review") || state.includes("pending") || nextGate.includes("review") || nextGate.includes("approval")) {
        entry.inReviewCount += 1;
      }
      if (state.includes("design") || state.includes("architect") || state.includes("implementation") || state.includes("develop") || nextGate.includes("design") || nextGate.includes("dev")) {
        entry.inDevelopmentCount += 1;
      }

      const validationStatus = normalize(feature.quality?.validationStatus);
      if (validationStatus.includes("fail") || validationStatus.includes("blocked") || validationStatus.includes("notready")) {
        entry.validationFailedCount += 1;
      }

      squads.set(squad, entry);
    }

    return Array.from(squads.values())
      .sort((a, b) => a.squad.localeCompare(b.squad))
      .map(
        (entry) => `
          <article class="squad-card">
            <div class="squad-title">
              <div>
                <div class="squad-label">Squad</div>
                <div class="name">${escapeHtml(entry.squad)}</div>
              </div>
              <span class="badge badge-info">${escapeHtml(formatCount(entry.featuresOwned))} feature${entry.featuresOwned === 1 ? "" : "s"}</span>
            </div>
            <div class="squad-stats">
              <div class="squad-stat"><div class="label">Blocked</div><div class="value">${escapeHtml(entry.blockedCount)}</div></div>
              <div class="squad-stat"><div class="label">In Review</div><div class="value">${escapeHtml(entry.inReviewCount)}</div></div>
              <div class="squad-stat"><div class="label">In Development</div><div class="value">${escapeHtml(entry.inDevelopmentCount)}</div></div>
              <div class="squad-stat"><div class="label">Validation Failed</div><div class="value">${escapeHtml(entry.validationFailedCount)}</div></div>
            </div>
          </article>`
      )
      .join("");
  }

  function traceabilityLinks(feature) {
    const links = [];
    const paths = feature.paths || {};
    if (paths.intent) links.push(`<a href="${escapeHtml(artifactHref(paths.intent))}" target="_blank" rel="noreferrer">Intent</a>`);
    if (paths.specification) links.push(`<a href="${escapeHtml(artifactHref(paths.specification))}" target="_blank" rel="noreferrer">Spec</a>`);
    if (paths.design) links.push(`<a href="${escapeHtml(artifactHref(paths.design))}" target="_blank" rel="noreferrer">Design</a>`);
    if (paths.tests) links.push(`<a href="${escapeHtml(artifactHref(paths.tests))}" target="_blank" rel="noreferrer">Tests</a>`);
    if (paths.validation) links.push(`<a href="${escapeHtml(artifactHref(paths.validation))}" target="_blank" rel="noreferrer">Validation</a>`);
    if (paths.release) links.push(`<a href="${escapeHtml(artifactHref(paths.release))}" target="_blank" rel="noreferrer">Release</a>`);
    if (!links.length) return '<span class="small">Missing</span>';
    return `<div class="chip-row" style="margin-top:0">${links.map((item) => `<span class="chip chip-muted">${item}</span>`).join("")}</div>`;
  }

  function traceabilityRow(feature) {
    const evidence = feature.evidence?.githubValidationEvidence || feature.evidence?.validationStatus || "Not available";
    return `
      <tr class="${feature.focus ? "focus-row" : ""}">
        <td><strong>${escapeHtml(feature.feature)}</strong><div class="small">${escapeHtml(feature.featureId)}</div></td>
        <td>${escapeHtml(feature.intentId || "Missing")}</td>
        <td>${escapeHtml(feature.specId || "Missing")}</td>
        <td>${escapeHtml(feature.designId || "Missing")}</td>
        <td>${escapeHtml(feature.testId || "Missing")}</td>
        <td>${escapeHtml(feature.jiraKey || "Missing")}</td>
        <td>${escapeHtml(feature.confluencePageId || "Missing")}</td>
        <td>${escapeHtml(feature.traceabilityId || "Missing")}</td>
        <td>${traceabilityLinks(feature)}</td>
        <td>${escapeHtml(evidence)}</td>
      </tr>`;
  }

  function renderTraceability(features) {
    return `
      <thead>
        <tr>
          <th>Feature ID</th>
          <th>Intent ID</th>
          <th>Specification ID</th>
          <th>Design ID</th>
          <th>Test ID</th>
          <th>Jira Issue</th>
          <th>Confluence Page</th>
          <th>Traceability ID</th>
          <th>Git Artifacts</th>
          <th>GitHub Validation</th>
        </tr>
      </thead>
      <tbody>${features.map(traceabilityRow).join("")}</tbody>`;
  }

  function qualityRow(feature) {
    const q = feature.quality || {};
    return `
      <tr class="${feature.focus ? "focus-row" : ""}">
        <td><strong>${escapeHtml(feature.feature)}</strong><div class="small">${escapeHtml(feature.featureId)}</div></td>
        <td>${q.intentPresent ? asChip("Present", "badge-ok") : asChip("Missing", "badge-danger")}</td>
        <td>${q.specificationPresent ? asChip("Present", "badge-ok") : asChip("Missing", "badge-danger")}</td>
        <td>${q.designPresent ? asChip("Present", "badge-ok") : asChip("Missing", "badge-danger")}</td>
        <td>${q.testsPresent ? asChip("Present", "badge-ok") : asChip("Missing", "badge-danger")}</td>
        <td>${q.openapiPresent ? asChip("Present", "badge-ok") : asChip("Missing", "badge-danger")}</td>
        <td>${q.traceabilityPresent ? asChip("Present", "badge-ok") : asChip("Missing", "badge-danger")}</td>
        <td><span class="${badgeClass(q.validationStatus)}">${escapeHtml(q.validationStatus)}</span></td>
        <td><span class="${badgeClass(q.releaseReadinessStatus)}">${escapeHtml(q.releaseReadinessStatus)}</span></td>
      </tr>`;
  }

  function renderQuality(features) {
    return `
      <thead>
        <tr>
          <th>Feature</th>
          <th>Intent</th>
          <th>Specification</th>
          <th>Design</th>
          <th>Tests</th>
          <th>OpenAPI</th>
          <th>Traceability</th>
          <th>Validation Status</th>
          <th>Release Readiness</th>
        </tr>
      </thead>
      <tbody>${features.map(qualityRow).join("")}</tbody>`;
  }

  function interventionReasonList(feature) {
    const reasons = Array.isArray(feature.interventions) ? feature.interventions : [];
    return reasons
      .filter((item, index, array) => array.indexOf(item) === index)
      .sort((left, right) => interventionPriority.indexOf(left) - interventionPriority.indexOf(right));
  }

  function renderIntervention(feature) {
    const reasons = interventionReasonList(feature);
    const primaryReason = reasons[0] || "missing-approval";
    const reasonText = interventionReasonText[primaryReason] || "Review required.";
    const actionText = interventionActionText[primaryReason] || "Review the feature and decide the next governance step.";
    const focusBadge = feature.focus ? `<span class="badge badge-info">Demo focus</span>` : "";

    return `
      <article class="intervention-card">
        <div class="header">
          <div>
            <div class="feature">${escapeHtml(feature.feature)}</div>
            <div class="intervention-meta">${escapeHtml(feature.domain)} / ${escapeHtml(feature.capability)}</div>
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:flex-end">
            <span class="${badgeClass(featureState(feature))}">${escapeHtml(featureState(feature))}</span>
            ${focusBadge}
          </div>
        </div>
        <div class="intervention-grid">
          <div class="intervention-tile">
            <div class="label">Owner role</div>
            <div class="value">${escapeHtml(featureOwnerRole(feature) || "Missing owner")}</div>
          </div>
          <div class="intervention-tile">
            <div class="label">Days in state</div>
            <div class="value">${escapeHtml(featureDaysInState(feature))}</div>
          </div>
          <div class="intervention-tile">
            <div class="label">Current gate</div>
            <div class="value">${escapeHtml(featureNextGate(feature) || "Missing")}</div>
          </div>
          <div class="intervention-tile">
            <div class="label">Traceability</div>
            <div class="value">${escapeHtml(feature.traceabilityId || "Missing")}</div>
          </div>
          <div class="intervention-tile">
            <div class="label">Blocked reason</div>
            <div class="value">${escapeHtml(featureBlockedReason(feature) || "None")}</div>
          </div>
          <div class="intervention-tile">
            <div class="label">Last updated</div>
            <div class="value">${escapeHtml(formatTimestamp(featureLastUpdated(feature)))}</div>
          </div>
        </div>
        <div class="intervention-actions">
          <div class="intervention-action">
            <span class="bullet"></span>
            <div class="text"><strong>Reason:</strong> ${escapeHtml(reasonText)}</div>
          </div>
          <div class="intervention-action">
            <span class="bullet"></span>
            <div class="text"><strong>Suggested PM action:</strong> ${escapeHtml(actionText)}</div>
          </div>
        </div>
        <div class="chip-row" style="margin-top:12px">
          ${reasons.map((item) => asChip(item, item.includes("missing") || item.includes("failed") || item.includes("blocked") ? "badge-danger" : "badge-warn")).join("")}
        </div>
      </article>`;
  }

  function renderInterventions(features) {
    const items = features
      .filter((feature) => Array.isArray(feature.interventions) && feature.interventions.length > 0)
      .sort(
        (left, right) =>
          Number(Boolean(right.focus)) - Number(Boolean(left.focus)) ||
          Number(Boolean(right.blocked)) - Number(Boolean(left.blocked)) ||
          featureDaysInState(right) - featureDaysInState(left)
      );

    document.getElementById("intervention-count").textContent = `${items.length} item${items.length === 1 ? "" : "s"}`;

    if (!items.length) {
      return '<div class="empty-state">No feature currently needs PM intervention.</div>';
    }

    return items.map(renderIntervention).join("");
  }

  function navLinks() {
    return Array.from(document.querySelectorAll("[data-nav-link]"));
  }

  function setActiveSection(sectionId) {
    const links = navLinks();
    const activeLink = [...links].reverse().find((link) => link.getAttribute("data-nav-link") === sectionId) || null;
    links.forEach((link) => {
      link.classList.toggle("active", link === activeLink);
    });
  }

  function installSectionObserver() {
    if (!("IntersectionObserver" in window)) return;
    const sections = Array.from(document.querySelectorAll("main section[id]"));
    if (!sections.length) return;

    if (window.__CONTROL_TOWER_SECTION_OBSERVER__) {
      window.__CONTROL_TOWER_SECTION_OBSERVER__.disconnect();
    }

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];
        if (visible) {
          setActiveSection(visible.target.id);
        }
      },
      { rootMargin: "-20% 0px -55% 0px", threshold: [0.15, 0.3, 0.45, 0.6] }
    );

    sections.forEach((section) => observer.observe(section));
    window.__CONTROL_TOWER_SECTION_OBSERVER__ = observer;
  }

  function updateRefreshState(data) {
    const generatedAt = formatTimestamp(data.generatedAt);
    const refreshedAt = new Date().toLocaleString();
    document.getElementById("generated-at").textContent = `Data generated ${generatedAt}`;
    document.getElementById("last-refreshed").textContent = `Last refreshed ${refreshedAt}`;
  }

  function updateRefreshMode() {
    const note = document.getElementById("refresh-note");
    const refreshMode = document.getElementById("refresh-mode");
    if (FILE_PROTOCOL) {
      refreshMode.textContent = "File view";
      note.textContent = "Open through a local HTTP server for 30-second auto-refresh. File:// uses the generated wrapper data and does not auto-refresh.";
      return;
    }

    refreshMode.textContent = "Local HTTP auto-refresh enabled";
    note.textContent = "Control Tower JSON reloads every 30 seconds while served from localhost.";
  }

  async function fetchData() {
    const response = await fetch("../build/dashboard/control-tower.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Failed to load dashboard data: ${response.status}`);
    }
    return response.json();
  }

  async function loadData() {
    if (window.__CONTROL_TOWER_DATA__ && FILE_PROTOCOL) {
      return window.__CONTROL_TOWER_DATA__;
    }

    try {
      return await fetchData();
    } catch (error) {
      if (window.__CONTROL_TOWER_DATA__) {
        return window.__CONTROL_TOWER_DATA__;
      }
      throw error;
    }
  }

  function renderDashboard(data) {
    const features = Array.isArray(data.features) ? data.features.slice() : [];
    const featured = selectFeaturedFeature(features);
    document.getElementById("featured-feature").innerHTML = renderFeaturedFeature(featured);
    document.getElementById("summary-grid").innerHTML = renderSummary(data.summary || {});
    document.getElementById("state-chips").innerHTML = renderStateChips(data.summary?.featuresByState || {});
    document.getElementById("pipeline-table").innerHTML = renderPipeline(features);
    document.getElementById("approval-queue-grid").innerHTML = renderApprovalQueue(data.approvalQueue || {});
    document.getElementById("squad-grid").innerHTML = renderSquadView(features);
    document.getElementById("traceability-table").innerHTML = renderTraceability(features);
    document.getElementById("quality-table").innerHTML = renderQuality(features);
    document.getElementById("intervention-list").innerHTML = renderInterventions(features);
    updateRefreshState(data);
    setActiveSection("pm-intervention");
    installSectionObserver();
  }

  function renderError(error) {
    const message = error instanceof Error ? error.message : String(error);
    document.getElementById("generated-at").textContent = "Dashboard unavailable";
    document.getElementById("last-refreshed").textContent = "Refresh unavailable";
    document.getElementById("summary-grid").innerHTML = `<div class="empty-state">${escapeHtml(message)}</div>`;
  }

  function startAutoRefresh() {
    if (FILE_PROTOCOL) return;
    if (window.__CONTROL_TOWER_REFRESH_TIMER__) {
      clearInterval(window.__CONTROL_TOWER_REFRESH_TIMER__);
    }
    window.__CONTROL_TOWER_REFRESH_TIMER__ = window.setInterval(() => {
      loadData().then(renderDashboard).catch(renderError);
    }, REFRESH_INTERVAL_MS);
  }

  navLinks().forEach((link) => {
    link.addEventListener("click", () => {
      setActiveSection(link.getAttribute("data-nav-link") || "pm-intervention");
    });
  });

  updateRefreshMode();
  loadData().then((data) => {
    renderDashboard(data);
    startAutoRefresh();
  }).catch(renderError);
})();
