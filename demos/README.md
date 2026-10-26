# Demo skill yang diminta lowongan QA (dibangun 26 Okt 2026)

Semua memakai situs/API demo **publik**, tanpa data perusahaan. Semua sudah dijalankan dan lulus.

| Skill | Folder | Hasil terverifikasi | Jalankan |
|---|---|---|---|
| k6 (load test) | `k6/` | 81 request, 0% gagal, p95 435 ms, threshold lulus | `k6 run quotes-load.js` |
| Selenium + Python (pytest) | `selenium-python/` | 4/4 lulus (headless Chrome) | `python3 -m pytest -q` |
| Cypress | `cypress/` | 4/4 lulus (Chrome) | `npm install && npx cypress run --browser chrome` |
| Python API test (pytest + requests) | `api-python/` | 11/11 lulus | `python3 -m pytest -q` |
| ERD dan UML | `erd-uml/` | ERD, use case, sequence, state, class dari `toko.db` (Mermaid + PDF) | buka `ERD dan UML Toko Mini.pdf` |
| Test case management | `test-management/` | 54 test case siap impor TestRail/Qase (BELUM diimpor, perlu akun) | lihat README di folder itu |

Belum ada: Java (JDK 17 terpasang, belum ada tes), Appium (Maestro sudah ada untuk mobile), Robot Framework, BrowserStack, TestRail/Qase yang benar-benar dipakai.
