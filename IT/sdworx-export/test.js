const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert.ok(script, 'Script del generatore non trovato');

function generator(company, employee, format = '7') {
  const nodes = new Map();
  const document = {
    querySelector(selector) {
      if (!nodes.has(selector)) nodes.set(selector, {
        addEventListener() {},
        value: '',
        checked: false,
        innerHTML: '',
      });
      return nodes.get(selector);
    },
    querySelectorAll() { return []; },
  };
  const field = (properties) => ({ addEventListener() {}, ...properties });
  nodes.set('#coAz', field({ value: company }));
  nodes.set('#empFormat', field({ value: format }));
  nodes.set('#hpd', field({ value: '8' }));
  nodes.set('#skipWknd', field({ checked: true }));
  nodes.set('#stateFilter', field({ value: 'Approvata' }));
  nodes.set('#period', field({ value: '' }));
  const context = vm.createContext({ document });
  vm.runInContext(script, context);
  context.employeeCode = employee;
  vm.runInContext(`
    state.col = { employee: 0, type: 1, start: 2, end: 3, dur: 4, stato: 5 };
    state.rows = [['Mario Rossi', 'Ferie', '2026-09-01', '2026-09-01', '1 giorno', 'Approvata']];
    state.emps.set('Mario Rossi', { code: employeeCode });
    state.types.set('Ferie', { code: 'FER' });
  `, context);
  return vm.runInContext('buildXml().xml', context);
}

test('azienda a 6 cifre e dipendente a 7 cifre nell’XML', () => {
  const xml = generator('9', '10');
  assert.match(xml, /<Dipendente CodAziendaUfficiale="000009" CodDipendenteUfficiale="0000010">/);
  assert.match(xml, /<Data>2026-09-01<\/Data>/);
});

test('codici già normalizzati restano invariati', () => {
  const xml = generator('000009', '0000010');
  assert.match(xml, /<Dipendente CodAziendaUfficiale="000009" CodDipendenteUfficiale="0000010">/);
});

test('si può scegliere un formato diverso quando richiesto', () => {
  assert.match(generator('9', '0000010', '6'), /CodDipendenteUfficiale="000010"/);
  assert.match(generator('9', '0000010', 'plain'), /CodDipendenteUfficiale="10"/);
});

test('sette cifre è il formato predefinito della pagina', () => {
  assert.match(html, /<option value="7" selected>7 cifre/);
});
