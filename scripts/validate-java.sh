#!/usr/bin/env bash
set -euo pipefail

if [[ -x "./mvnw" ]]; then
  ./mvnw test
  exit 0
fi

if [[ -f "pom.xml" ]] && command -v mvn >/dev/null 2>&1; then
  mvn test
  exit 0
fi

if [[ -x "./gradlew" ]]; then
  ./gradlew test
  exit 0
fi

if [[ -f "build.gradle" || -f "build.gradle.kts" ]] && command -v gradle >/dev/null 2>&1; then
  gradle test
  exit 0
fi

if ! command -v javac >/dev/null 2>&1; then
  echo "::error::No Java build tool found and javac is unavailable"
  exit 1
fi

main_sources=()
while IFS= read -r file; do
  main_sources+=("$file")
done < <(find src/main/java -name '*.java' -type f | sort 2>/dev/null || true)

test_sources=()
while IFS= read -r file; do
  test_sources+=("$file")
done < <(find src/test/java -name '*.java' -type f | sort 2>/dev/null || true)

if [[ "${#main_sources[@]}" -eq 0 ]]; then
  echo "No Java main sources found."
  exit 0
fi

classes_dir="${RUNNER_TEMP:-/tmp}/ai-sdlc-java-classes"
rm -rf "$classes_dir"
mkdir -p "$classes_dir"

javac -d "$classes_dir" "${main_sources[@]}"
echo "Java main sources compiled."

if [[ "${#test_sources[@]}" -eq 0 ]]; then
  echo "No Java test sources found."
  exit 0
fi

javac -cp "$classes_dir" -d "$classes_dir" "${test_sources[@]}"
echo "Java test sources compiled."

for test_source in "${test_sources[@]}"; do
  if grep -q "public static void main(String\\[\\] args)" "$test_source"; then
    test_class="${test_source#src/test/java/}"
    test_class="${test_class%.java}"
    test_class="${test_class//\//.}"
    java -cp "$classes_dir" "$test_class"
  fi
done

echo "Java validation passed."
