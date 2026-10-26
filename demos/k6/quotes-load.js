// Load test dasar dengan k6 pada API demo publik Grafana (quickpizza). Tidak ada data privat.
// Jalankan: k6 run quotes-load.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  scenarios: {
    smoke: { executor: 'shared-iterations', vus: 1, iterations: 3, maxDuration: '20s', exec: 'browse' },
    load: { executor: 'constant-vus', vus: 5, duration: '20s', startTime: '25s', exec: 'browse' },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],        // error kurang dari 1%
    http_req_duration: ['p(95)<1500'],     // 95% request di bawah 1,5 detik
    checks: ['rate>0.99'],
  },
};

const BASE = 'https://quickpizza.grafana.com';

export function browse() {
  const res = http.get(`${BASE}/api/quotes`);
  check(res, {
    'status 200': (r) => r.status === 200,
    'body punya quotes': (r) => Array.isArray(r.json('quotes')) && r.json('quotes').length > 0,
  });
  sleep(1);
}
