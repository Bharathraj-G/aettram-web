/* ============================================================
   ROI Calculator — Logic
   Step navigation, form validation, Quick ROI & Investment
   Analysis calculations with live result updates.
   ============================================================ */

(function () {
  'use strict';

  /* ---------- DOM refs ---------- */
  const steps     = document.querySelectorAll('.roi-step');
  const heroEl    = document.querySelector('.roi-hero');

  /* Step 1 */
  const btnContinue = document.getElementById('roi-continue');

  /* Step 2 */
  const cardQuick      = document.getElementById('roi-pick-quick');
  const cardInvestment = document.getElementById('roi-pick-investment');

  /* Step 3a — Quick ROI */
  const btnCalcQuick   = document.getElementById('roi-calc-quick');
  const btnChangeQuick = document.getElementById('roi-change-quick');

  /* Step 3b — Investment */
  const btnCalcInvest   = document.getElementById('roi-calc-invest');
  const btnChangeInvest = document.getElementById('roi-change-invest');
  const btnExploreInvest = document.getElementById('roi-explore-invest');

  let currentStep = 1;

  /* ---------- Helpers ---------- */
  function show(step) {
    steps.forEach(s => s.classList.remove('is-active'));
    const target = document.getElementById('roi-step-' + step);
    if (target) {
      target.classList.add('is-active');
      currentStep = step;
      window.scrollTo({ top: heroEl.offsetTop, behavior: 'smooth' });
    }
  }

  function val(id) {
    const el = document.getElementById(id);
    return el ? parseFloat(el.value) || 0 : 0;
  }

  function fmt(n) {
    if (n === Infinity || n === -Infinity || isNaN(n)) return '—';
    return '₹' + Math.round(n).toLocaleString('en-IN');
  }

  function fmtYears(n) {
    if (n === Infinity || n === -Infinity || isNaN(n) || n <= 0) return '—';
    return n.toFixed(1) + ' yrs';
  }

  function fmtPercent(n) {
    if (n === Infinity || n === -Infinity || isNaN(n)) return '—';
    return n.toFixed(1) + '%';
  }

  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  /* ---------- Step 1 — Validation ---------- */
  function validateStep1() {
    let valid = true;
    ['roi-name', 'roi-company', 'roi-email'].forEach(id => {
      const field = document.getElementById(id);
      const wrapper = field.closest('.roi-field');
      if (!field.value.trim()) {
        wrapper.classList.add('has-error');
        valid = false;
      } else {
        wrapper.classList.remove('has-error');
      }
    });
    // Basic email check
    const email = document.getElementById('roi-email');
    if (email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
      email.closest('.roi-field').classList.add('has-error');
      valid = false;
    }
    return valid;
  }

  if (btnContinue) {
    btnContinue.addEventListener('click', function () {
      if (validateStep1()) show('2');
    });
  }

  /* ---------- Step 2 — Analysis Picker ---------- */
  if (cardQuick) {
    cardQuick.addEventListener('click', function () {
      cardQuick.classList.add('is-selected');
      if (cardInvestment) cardInvestment.classList.remove('is-selected');
      setTimeout(function(){ show('3a'); }, 250);
    });
  }

  if (cardInvestment) {
    cardInvestment.addEventListener('click', function () {
      cardInvestment.classList.add('is-selected');
      if (cardQuick) cardQuick.classList.remove('is-selected');
      setTimeout(function(){ show('3b'); }, 250);
    });
  }

  /* ---------- Step 3a — Quick ROI Calculation ---------- */
  function calcQuickROI() {
    const opsBefore   = val('q-ops-before');
    const opsAfter    = val('q-ops-after');
    const costPerHr   = val('q-cost-hr');
    const hrsPerDay   = val('q-hrs-day');
    const daysPerYear = val('q-days-year');
    const investment  = val('q-investment');
    const addlContrib = val('q-contribution');
    const opCost      = val('q-op-cost');

    const annualLabourSaving = (opsBefore - opsAfter) * costPerHr * hrsPerDay * daysPerYear;
    const annualNetBenefit   = annualLabourSaving + addlContrib - opCost;
    const simplePayback      = annualNetBenefit > 0 ? investment / annualNetBenefit : Infinity;
    const fiveYearNet        = (annualNetBenefit * 5) - investment;

    setText('qr-labour-saving', fmt(annualLabourSaving));
    setText('qr-net-benefit',   fmt(annualNetBenefit));
    setText('qr-payback',       fmtYears(simplePayback));
    setText('qr-5yr-net',       fmt(fiveYearNet));

    // "What this means" narrative
    const noteEl = document.getElementById('qr-note');
    if (noteEl) {
      if (annualNetBenefit > 0) {
        noteEl.textContent = 'Automation saves ' + fmt(annualLabourSaving) + ' in labour annually. After operating costs, the net annual benefit is ' + fmt(annualNetBenefit) + ', paying back the investment in about ' + fmtYears(simplePayback) + '.';
      } else {
        noteEl.textContent = 'Enter your assumptions and calculate.';
      }
    }
  }

  if (btnCalcQuick) {
    btnCalcQuick.addEventListener('click', calcQuickROI);
  }
  if (btnChangeQuick) {
    btnChangeQuick.addEventListener('click', function () { show('2'); });
  }
  if (btnExploreInvest) {
    btnExploreInvest.addEventListener('click', function () {
      // Deselect Quick, select Investment
      if (cardQuick) cardQuick.classList.remove('is-selected');
      if (cardInvestment) cardInvestment.classList.add('is-selected');
      show('3b');
    });
  }

  /* ---------- Step 3b — Investment Analysis Calculation ---------- */
  function calcInvestmentAnalysis() {
    // Inputs
    const investment      = val('i-investment');
    const usefulLife      = val('i-useful-life');
    const daysPerYear     = val('i-days-year');
    const shiftsPerDay    = val('i-shifts-day');
    const hrsPerShift     = val('i-hrs-shift');
    const curOps          = val('i-cur-ops');
    const autoOps         = val('i-auto-ops');
    const costPerHr       = val('i-cost-hr');
    const curOutput       = val('i-cur-output');
    const autoOutput      = val('i-auto-output');
    const marginPerPart   = val('i-margin');
    const curReject       = val('i-cur-reject') / 100;
    const autoReject      = val('i-auto-reject') / 100;
    const curDowntime     = val('i-cur-downtime');
    const autoDowntime    = val('i-auto-downtime');
    const downtimeValue   = val('i-downtime-value');

    // Escalation
    const wageEsc         = val('i-wage-esc') / 100;
    const utilEsc         = val('i-util-esc') / 100;
    const maintenance     = val('i-maintenance');
    const maintEsc        = val('i-maint-esc') / 100;
    const otherOpCost     = val('i-other-op');
    const otherEsc        = val('i-other-esc') / 100;

    // Financing
    const finMethod       = document.getElementById('i-fin-method').value;
    const downPayment     = val('i-down-payment');
    const loanInterest    = val('i-loan-interest') / 100;
    const loanTenure      = val('i-loan-tenure');
    const discountRate    = val('i-discount-rate') / 100;

    // --- Year 1 Calculations ---
    const annualHrs = hrsPerShift * shiftsPerDay * daysPerYear;

    // Labour saving
    const labourSaving = (curOps - autoOps) * costPerHr * annualHrs;

    // Throughput gain
    const throughputGain = (autoOutput - curOutput) * marginPerPart * annualHrs;

    // Quality saving
    const qualitySaving = (curReject - autoReject) * curOutput * marginPerPart * annualHrs;

    // Downtime saving (monthly values × 12)
    const downtimeSaving = (curDowntime - autoDowntime) * downtimeValue * 12;

    const totalAnnualBenefit = labourSaving + throughputGain + qualitySaving + downtimeSaving;

    // Operating costs year 1
    const year1OpCost = maintenance + otherOpCost;
    const year1NetBenefit = totalAnnualBenefit - year1OpCost;

    // Simple payback
    const simplePayback = year1NetBenefit > 0 ? investment / year1NetBenefit : Infinity;

    // --- Financing ---
    let emi = 0;
    let totalLoanInterest = 0;
    if (finMethod === 'bank-loan' && loanInterest > 0 && loanTenure > 0) {
      const principal = Math.max(investment - downPayment, 0);
      const r = loanInterest / 12;
      const n = loanTenure * 12;
      if (r > 0 && n > 0) {
        emi = principal * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
        totalLoanInterest = (emi * n) - principal;
      }
    }

    // --- NPV ---
    let npv = -investment;
    for (let yr = 1; yr <= usefulLife; yr++) {
      const escLabour     = labourSaving * Math.pow(1 + wageEsc, yr - 1);
      const escThroughput = throughputGain;
      const escQuality    = qualitySaving;
      const escDowntime   = downtimeSaving;
      const escBenefit    = escLabour + escThroughput + escQuality + escDowntime;

      const escMaint  = maintenance * Math.pow(1 + maintEsc, yr - 1);
      const escOther  = otherOpCost * Math.pow(1 + otherEsc, yr - 1);
      const escOpCost = escMaint + escOther;

      const netCashFlow = escBenefit - escOpCost;
      npv += netCashFlow / Math.pow(1 + discountRate, yr);
    }

    // --- IRR (bisection) ---
    function npvAtRate(rate) {
      let v = -investment;
      for (let yr = 1; yr <= usefulLife; yr++) {
        const escLabour = labourSaving * Math.pow(1 + wageEsc, yr - 1);
        const escBenefit = escLabour + throughputGain + qualitySaving + downtimeSaving;
        const escMaint = maintenance * Math.pow(1 + maintEsc, yr - 1);
        const escOther = otherOpCost * Math.pow(1 + otherEsc, yr - 1);
        const net = escBenefit - escMaint - escOther;
        v += net / Math.pow(1 + rate, yr);
      }
      return v;
    }

    let irr = NaN;
    let lo = -0.5, hi = 5.0;
    const npvLo = npvAtRate(lo);
    const npvHi = npvAtRate(hi);
    if (npvLo * npvHi < 0) {
      for (let iter = 0; iter < 100; iter++) {
        const mid = (lo + hi) / 2;
        const npvMid = npvAtRate(mid);
        if (Math.abs(npvMid) < 1) { irr = mid * 100; break; }
        if (npvMid * npvLo < 0) { hi = mid; }
        else { lo = mid; }
        irr = mid * 100;
      }
    }

    // --- Update UI ---
    setText('ir-y1-benefit',     fmt(year1NetBenefit));
    setText('ir-payback',        fmtYears(simplePayback));
    setText('ir-emi',            finMethod === 'bank-loan' ? fmt(emi) : '—');
    setText('ir-loan-interest',  finMethod === 'bank-loan' ? fmt(totalLoanInterest) : '—');
    setText('ir-npv',            fmt(npv));
    setText('ir-irr',            isNaN(irr) ? '—' : fmtPercent(irr));
  }

  if (btnCalcInvest) {
    btnCalcInvest.addEventListener('click', calcInvestmentAnalysis);
  }
  if (btnChangeInvest) {
    btnChangeInvest.addEventListener('click', function () { show('2'); });
  }

  /* ---------- Toggle financing fields ---------- */
  const finMethod = document.getElementById('i-fin-method');
  const finFields = document.getElementById('roi-fin-fields');
  if (finMethod && finFields) {
    function toggleFinFields() {
      if (finMethod.value === 'bank-loan') {
        finFields.style.display = '';
      } else {
        finFields.style.display = 'none';
      }
    }
    finMethod.addEventListener('change', toggleFinFields);
    toggleFinFields();
  }

  /* ---------- Init — show step 1 ---------- */
  show('1');

})();
