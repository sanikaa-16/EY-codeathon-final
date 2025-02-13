import { useState, useEffect } from "react";
import axios from "axios";

function Users() {
    const [users, setUsers] = useState([]);

    const fetchUsers = async () => {
        try {
            const response = await axios.get("http://localhost:8080/users");
            setUsers(response.data);
        } catch (error) {
            console.error("Error fetching users:", error);
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <div>
            <h2>Users</h2>
            <ul>
                {users.map(({ user_id, role, college_email, created_at }) => (
                    <li key={user_id}>
                        <strong>{role}</strong> - {college_email} (Created: {created_at})
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Users;
