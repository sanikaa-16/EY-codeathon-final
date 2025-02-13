import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { BookOpen, Users, GraduationCap, FolderKanban, User, TrendingUp, Menu, LogOut } from 'lucide-react';

const HomePage = ({ userId, userName }) => {
    const [hoveredCard, setHoveredCard] = useState(null);
    const [sidebarOpen, setSidebarOpen] = useState(false);
    const [showDropdown, setShowDropdown] = useState(false);
    const navigate = useNavigate();

    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };

    const handleLogout = () => {
        localStorage.removeItem('userToken'); // Clear stored session data if needed
        navigate('/'); // Redirect to landing page
    };

    const menuItems = [
        { id: 1, title: 'My Profile', icon: <User size={24} />, link: `/profile/${userId}` },
        { id: 2, title: 'My Projects', icon: <BookOpen size={24} />, link: `/myprojects/${userId}` },
        { id: 3, title: 'Student Directory', icon: <GraduationCap size={24} />, link: '/student-list' },
        { id: 4, title: 'Faculty Directory', icon: <Users size={24} />, link: '/faculty-list' },
        { id: 5, title: 'Project Repository', icon: <FolderKanban size={24} />, link: '/projects-list' },
        { id: 6, title: 'Projects I belong to', icon: <FolderKanban size={24} />, link: `/projectsmepart/${userId}` },
        { id: 7, title: 'Charts', icon: <TrendingUp size={24} />, link: `/charts` }
    ];

    return (
        <div className="flex min-h-screen bg-[#F4F4F8]">
            {/* Sidebar */}
            <div className={`fixed inset-y-0 left-0 w-64 bg-[#6B47DC] text-white p-6 transform ${sidebarOpen ? "translate-x-0" : "-translate-x-full"} transition-transform md:translate-x-0`}>
                <h2 className="text-2xl font-bold">Dashboard</h2>
                <ul className="mt-6 space-y-4">
                    {menuItems.map((item) => (
                        <li key={item.id}>
                            <Link to={item.link} className="flex items-center gap-3 p-2 hover:bg-[#D9C2FF] hover:text-black rounded-md">
                                {item.icon}
                                {item.title}
                            </Link>
                        </li>
                    ))}
                </ul>
            </div>

            {/* Main Content */}
            <div className="flex-1 ml-0 md:ml-64 p-8 relative">
                {/* Navbar */}
                <div className="flex justify-between items-center mb-6 relative">
                    <button className="md:hidden text-[#6B47DC]" onClick={toggleSidebar}>
                        <Menu size={28} />
                    </button>
                    <h1 className="text-3xl font-bold text-[#6B47DC]">Project Information System</h1>

                    {/* User Icon & Dropdown */}
                    <div className="relative">
                        <button className="flex items-center gap-3" onClick={() => setShowDropdown(!showDropdown)}>
                            <User size={32} className="text-[#6B47DC] cursor-pointer" />
                            <span className="text-lg font-medium">{userName}</span>
                        </button>
                        
                        {showDropdown && (
                            <div className="absolute right-0 mt-2 w-40 bg-white shadow-md rounded-md overflow-hidden">
                                <button 
                                    onClick={handleLogout} 
                                    className="flex items-center gap-2 px-4 py-2 w-full text-red-600 hover:bg-gray-100"
                                >
                                    <LogOut size={20} />
                                    Logout
                                </button>
                            </div>
                        )}
                    </div>
                </div>

                {/* Centered Greeting */}
                <div className="flex justify-center items-center h-40">
                    <h2 className="text-2xl font-semibold text-[#6B47DC]">
                        Hello, {userName} (ID: {userId})
                    </h2>
                </div>

                {/* Card Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {menuItems.map((item) => (
                        <Link
                            key={item.id}
                            to={item.link}
                            className="transform transition-all duration-300 hover:scale-105"
                            onMouseEnter={() => setHoveredCard(item.id)}
                            onMouseLeave={() => setHoveredCard(null)}
                        >
                            <div className="relative rounded-xl p-6 h-48 bg-[#D9C2FF] text-black overflow-hidden shadow-md">
                                <div className="absolute top-0 right-0 p-4 opacity-10">
                                    {item.icon}
                                </div>
                                <div className="relative z-10">
                                    <div className="flex items-center gap-3 mb-3">
                                        {item.icon}
                                        <h3 className="text-xl font-semibold">{item.title}</h3>
                                    </div>
                                    <p className={`transition-opacity duration-300 ${hoveredCard === item.id ? 'opacity-100' : 'opacity-80'}`}>
                                        Explore this section
                                    </p>
                                </div>
                                <div className={`absolute bottom-0 right-0 w-32 h-32 transform translate-x-16 translate-y-16 bg-white opacity-10 rounded-full transition-transform duration-300 ${hoveredCard === item.id ? 'scale-150' : 'scale-100'}`} />
                            </div>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default HomePage;
