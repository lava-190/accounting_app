// app/static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    const settingsBar = document.getElementById('settings-bar');
    const toggleSettingsBtn = document.getElementById('toggle-settings');
    const toggleModeBtn = document.getElementById('toggle-mode');
    const addUnitBtn = document.getElementById('add-unit-btn');
    const unitTableBody = document.querySelector('#unit-table tbody');
    const grandTotalDisplay = document.getElementById('grand-total');
  
    // Toggle the visibility of the settings bar
    toggleSettingsBtn.addEventListener('click', () => {
      settingsBar.classList.toggle('collapsed');
    });
  
    // Toggle dark/light mode
    toggleModeBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
    });
  
    // Fetch existing units from the backend
    function fetchUnits() {
      fetch('/api/units')
        .then(response => response.json())
        .then(data => {
          renderUnits(data);
          updateGrandTotal(data);
        });
    }
  
    // Render unit rows in the table
    function renderUnits(units) {
      unitTableBody.innerHTML = '';
      units.forEach(unit => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${unit.name}</td>
          <td>$${unit.current_price.toFixed(2)}</td>
          <td>
            <input type="number" value="1" min="1" class="quantity-input" data-price="${unit.current_price}" />
          </td>
          <td class="row-total">$${unit.current_price.toFixed(2)}</td>
          <td>
            <button class="edit-btn" data-id="${unit.id}">Edit</button>
            <button class="delete-btn" data-id="${unit.id}">Delete</button>
          </td>
        `;
        unitTableBody.appendChild(row);
      });
    }
  
    // Update the grand total
    function updateGrandTotal(units) {
      // Calculate table totals based on each unit's default quantity (1) initially
      const prices = units.map(u => u.current_price);
      fetch('/api/calculate_total', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ prices: prices })
      })
        .then(response => response.json())
        .then(data => {
          grandTotalDisplay.innerText = `Grand Total: $${data.total.toFixed(2)}`;
        });
    }
  
    // Add a new unit (simplified inline prompt; consider a modal for production)
    addUnitBtn.addEventListener('click', () => {
      const name = prompt('Enter unit name:');
      const price = parseFloat(prompt('Enter unit price:'));
      if (name && !isNaN(price)) {
        fetch('/api/units', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ name, current_price: price, category: '' })
        })
          .then(response => response.json())
          .then(() => fetchUnits());
      }
    });
  
    // Initially fetch units
    fetchUnits();
  });
  