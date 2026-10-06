/**
 * Jaymani Krishi Sewa - Vanilla JS Logic
 * Handles View Navigation, Auth, and Data Fetching
 */

const API_BASE = 'http://localhost:5000/api';
let currentUser = null;

// DOM Elements
const navBtns = document.querySelectorAll('.navigate-btn, .nav-btn');
const views = document.querySelectorAll('.view');
const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const loginForm = document.getElementById('login-form');
const productsGrid = document.getElementById('products-grid');
const searchInput = document.getElementById('search-input');
const categoryFilter = document.getElementById('category-filter');
const toastEl = document.getElementById('toast');
const toastMsg = document.getElementById('toast-message');

// Fallback Mock Data in case Flask API is not running
const MOCK_PRODUCTS = [
    { id: 1, name: 'Urea Fertilizer 50kg', category: 'Fertilizer', price: 1200, vendor_name: 'Suresh Vendor', vendor_location: 'Market B', stock: 50 },
    { id: 2, name: 'Wheat Seeds (Premium)', category: 'Seeds', price: 800, vendor_name: 'Suresh Vendor', vendor_location: 'Market B', stock: 100 },
    { id: 3, name: 'Organic Compost', category: 'Fertilizer', price: 450, vendor_name: 'Ramesh Agro', vendor_location: 'Village A', stock: 200 }
];

let currentProducts = [];

/* =========================================
   NAVIGATION & SPA LOGIC
   ========================================= */
navBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = btn.getAttribute('data-target');
        
        // Protect marketplace route
        if (targetId === 'marketplace-view' && !currentUser) {
            showToast("Please login first to view the marketplace.", true);
            switchView('login-view');
            return;
        }

        if (targetId) switchView(targetId);
    });
});

function switchView(targetId) {
    // Hide all
    views.forEach(view => {
        view.classList.remove('active-view');
        view.classList.add('hidden-view');
    });

    // Show target
    const targetView = document.getElementById(targetId);
    if(targetView) {
        targetView.classList.remove('hidden-view');
        targetView.classList.add('active-view');
    }

    // Update nav highlights
    document.querySelectorAll('.nav-links .nav-btn').forEach(btn => btn.classList.remove('active'));
    const activeNav = document.querySelector(`.nav-links .nav-btn[data-target="${targetId}"]`);
    if(activeNav && targetId !== 'login-view') {
        activeNav.classList.add('active');
    }

    // specific view logic
    if (targetId === 'marketplace-view') {
        fetchProducts();
    }
}

/* =========================================
   AUTHENTICATION LOGIC
   ========================================= */
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorEl = document.getElementById('login-error');

    errorEl.classList.add('hidden');
    
    try {
        const res = await fetch(`${API_BASE}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        
        const data = await res.json();
        
        if (res.ok) {
            handleLoginSuccess(data);
        } else {
            // Fallback for mock/demo if API is down
            if (email === 'farmer@jaymani.com' && password === 'farmer123') {
                handleLoginSuccess({ id: 2, name: 'Ramesh Farmer', role: 'farmer' });
            } else {
                errorEl.textContent = data.error || "Login failed.";
                errorEl.classList.remove('hidden');
            }
        }
    } catch (err) {
        console.warn("API not reachable, using mock fallback.");
        if (email === 'farmer@jaymani.com' && password === 'farmer123') {
            handleLoginSuccess({ id: 2, name: 'Ramesh Farmer', role: 'farmer' });
        } else {
            errorEl.textContent = "Server disconnected and invalid demo credentials.";
            errorEl.classList.remove('hidden');
        }
    }
});

function handleLoginSuccess(user) {
    currentUser = user;
    loginBtn.classList.add('hidden');
    logoutBtn.classList.remove('hidden');
    showToast(`Welcome back, ${user.name}!`);
    switchView('marketplace-view');
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault();
    currentUser = null;
    loginBtn.classList.remove('hidden');
    logoutBtn.classList.add('hidden');
    showToast("Logged out successfully.");
    switchView('home-view');
});

/* =========================================
   MARKETPLACE & DATA LOGIC
   ========================================= */
async function fetchProducts() {
    productsGrid.innerHTML = '<p>Loading products...</p>';
    try {
        const res = await fetch(`${API_BASE}/products`);
        if (res.ok) {
            currentProducts = await res.json();
        } else {
            throw new Error("Failed to fetch");
        }
    } catch (err) {
        console.warn("Using mock products.");
        currentProducts = MOCK_PRODUCTS;
    }
    renderProducts(currentProducts);
}

function renderProducts(products) {
    productsGrid.innerHTML = '';
    
    if (products.length === 0) {
        productsGrid.innerHTML = '<p>No products found.</p>';
        return;
    }

    products.forEach(p => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <span class="product-category">${p.category}</span>
            <h3 class="product-title">${p.name}</h3>
            <div class="product-vendor">
                <span>🏪</span> ${p.vendor_name} (${p.vendor_location})
            </div>
            <div class="product-price">₹${p.price}</div>
            <button class="btn btn-primary w-100" onclick="orderProduct(${p.id}, ${p.vendor_id || 3}, ${p.price}, '${p.name}')">
                Buy Now
            </button>
        `;
        productsGrid.appendChild(card);
    });
}

// Global function for inline onclick
window.orderProduct = async function(productId, vendorId, price, name) {
    if(!currentUser) return;
    
    try {
        const res = await fetch(`${API_BASE}/orders`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                farmer_id: currentUser.id, 
                vendor_id: vendorId, 
                total: price 
            })
        });
        
        if (res.ok) {
            showToast(`Order placed for ${name}!`);
        } else {
            throw new Error();
        }
    } catch (err) {
        showToast(`Demo: Order placed for ${name}! (Mock)`);
    }
};

/* =========================================
   FILTER & SEARCH LOGIC
   ========================================= */
function filterProducts() {
    const searchTerm = searchInput.value.toLowerCase();
    const category = categoryFilter.value;

    const filtered = currentProducts.filter(p => {
        const matchSearch = p.name.toLowerCase().includes(searchTerm) || p.vendor_name.toLowerCase().includes(searchTerm);
        const matchCategory = category === 'All' || p.category === category;
        return matchSearch && matchCategory;
    });

    renderProducts(filtered);
}

searchInput.addEventListener('input', filterProducts);
categoryFilter.addEventListener('change', filterProducts);

/* =========================================
   UI UTILS
   ========================================= */
let toastTimeout;
function showToast(msg, isError = false) {
    toastMsg.textContent = msg;
    toastEl.style.backgroundColor = isError ? 'var(--clr-error)' : 'var(--clr-primary-dark)';
    toastEl.classList.add('show');
    toastEl.classList.remove('hidden');
    
    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
        toastEl.classList.remove('show');
        setTimeout(() => toastEl.classList.add('hidden'), 300);
    }, 3000);
}
