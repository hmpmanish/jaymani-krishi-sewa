import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

frontend_dir = 'frontend'

tailwind_config = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#166534", // Green 800
        secondary: "#4ade80", // Green 400
      }
    },
  },
  plugins: [],
}
"""

index_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

body {
    background-color: #f8fafc;
}
"""

main_jsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter } from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)
"""

app_jsx = """import React, { useState } from 'react'
import { Routes, Route, useNavigate, Navigate } from 'react-router-dom'

export default function App() {
  const [user, setUser] = useState(null);
  
  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-primary text-white p-4 flex justify-between items-center shadow-md">
        <h1 className="text-xl font-bold">Jaymani Krishi Sewa</h1>
        <nav className="flex gap-4">
            <a href="/" className="hover:text-secondary">Home</a>
            {!user && <a href="/login" className="hover:text-secondary">Login</a>}
            {user && <span className="font-semibold">Welcome, {user.name} ({user.role})</span>}
            {user && <button onClick={() => setUser(null)} className="hover:text-secondary">Logout</button>}
        </nav>
      </header>

      <main className="flex-grow p-4 md:p-8">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login setUser={setUser} />} />
          <Route path="/dashboard" element={
            user ? (
                user.role === 'admin' ? <AdminDashboard user={user}/> :
                user.role === 'farmer' ? <FarmerDashboard user={user}/> :
                <VendorDashboard user={user}/>
            ) : <Navigate to="/login" />
          } />
        </Routes>
      </main>

      <footer className="bg-gray-800 text-white p-4 text-center">
        &copy; 2026 Jaymani Krishi Sewa - "बीज से समृद्धि तक"
      </footer>
    </div>
  )
}

function Home() {
    const navigate = useNavigate();
    return (
        <div className="text-center mt-10">
            <h2 className="text-4xl font-bold text-primary mb-4">Digital Agritech Marketplace for Farmers & Local Vendors</h2>
            <p className="text-lg text-gray-600 mb-8">Connect with nearby agricultural suppliers, discover products, manage orders, and maintain digital credit records — all in one platform.</p>
            <div className="flex justify-center gap-4">
                <button onClick={() => navigate('/login')} className="bg-primary text-white px-6 py-3 rounded-lg shadow-lg hover:bg-green-900">Explore Products</button>
                <button onClick={() => navigate('/login')} className="bg-secondary text-primary font-bold px-6 py-3 rounded-lg shadow-lg hover:bg-green-500">Join as Vendor</button>
            </div>
        </div>
    )
}

function Login({ setUser }) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch('http://localhost:5000/api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            const data = await res.json();
            if (res.ok) {
                setUser(data);
                navigate('/dashboard');
            } else {
                setError(data.error);
            }
        } catch (err) {
            setError("Server connection failed");
        }
    };

    return (
        <div className="max-w-md mx-auto bg-white p-8 border rounded-lg shadow-md mt-10">
            <h2 className="text-2xl font-bold text-center mb-6">Login</h2>
            {error && <p className="text-red-500 text-center mb-4">{error}</p>}
            <form onSubmit={handleLogin} className="flex flex-col gap-4">
                <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} className="border p-2 rounded" required />
                <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} className="border p-2 rounded" required />
                <button type="submit" className="bg-primary text-white p-2 rounded hover:bg-green-900">Login</button>
            </form>
            <div className="mt-4 text-sm text-gray-500">
                <p>Demo Accounts:</p>
                <p>Admin: admin@jaymani.com / admin123</p>
                <p>Farmer: farmer@jaymani.com / farmer123</p>
                <p>Vendor: vendor@jaymani.com / vendor123</p>
            </div>
        </div>
    )
}

function FarmerDashboard({ user }) {
    const [products, setProducts] = useState([]);
    
    React.useEffect(() => {
        fetch('http://localhost:5000/api/products')
            .then(res => res.json())
            .then(data => setProducts(data));
    }, []);

    const orderProduct = async (product) => {
        await fetch('http://localhost:5000/api/orders', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ farmer_id: user.id, vendor_id: product.vendor_id, total: product.price })
        });
        alert(`Order placed for ${product.name}!`);
    };

    return (
        <div>
            <h2 className="text-2xl font-bold mb-4">Farmer Dashboard - Hyper-Local Discovery</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {products.map(p => (
                    <div key={p.id} className="bg-white p-4 border rounded shadow-md">
                        <h3 className="font-bold text-lg">{p.name}</h3>
                        <p className="text-sm text-gray-500">{p.category}</p>
                        <p className="font-bold text-primary mt-2">₹{p.price}</p>
                        <p className="text-sm">Vendor: {p.vendor_name} ({p.vendor_location})</p>
                        <p className="text-sm">Stock: {p.stock}</p>
                        <button onClick={() => orderProduct(p)} className="mt-4 bg-primary text-white px-4 py-2 rounded w-full">Buy Now (Add to Cart)</button>
                    </div>
                ))}
            </div>
        </div>
    )
}

function VendorDashboard({ user }) {
    return (
        <div>
            <h2 className="text-2xl font-bold mb-4">Vendor Dashboard - Inventory</h2>
            <p>Welcome to the Vendor Inventory Management System.</p>
            <p className="mt-2 text-gray-600">Here vendors can view their active catalog, add products, and manage orders.</p>
        </div>
    )
}

function AdminDashboard({ user }) {
    return (
        <div>
            <h2 className="text-2xl font-bold mb-4">Admin Dashboard</h2>
            <p>Platform Statistics and Management.</p>
            <p className="mt-2 text-gray-600">Admins can monitor orders, bahi-khata records, and manage platform data.</p>
        </div>
    )
}
"""

create_file(os.path.join(frontend_dir, 'tailwind.config.js'), tailwind_config)
create_file(os.path.join(frontend_dir, 'src', 'index.css'), index_css)
create_file(os.path.join(frontend_dir, 'src', 'main.jsx'), main_jsx)
create_file(os.path.join(frontend_dir, 'src', 'App.jsx'), app_jsx)

print("Frontend files generated successfully.")
