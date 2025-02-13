import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, useParams } from "react-router-dom";
import LoginSignUp from "./Login";
import HomePage from "./HomePage";
import ProfilePage from "./profile"; // Renamed to match the import
import StudentDetails from "./StudentDetails";
import FacultyDetails from "./FacultyDetails";
import MyProjects from "./MyProjects";
import AddProject from "./AddProject";
import ProjectList from "./project-list";
import StudentList from "./student-list";
import FacultyList from "./faculty-list";
import UserProjects from "./projectsmepartof";
import ProjectDashboard from "./charts";
function App() {
  const [userId, setUserId] = useState(null); // Tracks the logged-in user's ID

  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-blue-100 to-purple-100">
        <Routes>
          {/* Default Route */}
          <Route
            path="/"
            element={
              <LoginSignUp onLoginSuccess={(id) => setUserId(id)} />
            }
          />
          {/* Home Route */}

          <Route
            path="/home"
            element={
              userId ? (
                <HomePage userId={userId} />
              ) : (
                <div className="text-center">Please log in to access this page.</div>
              )
            }
          />
          {/* stuentdetails */}
          <Route
            path="/studentdetails"
            element={<StudentDetails userId={userId} />}
          />
          {/*facultydetaiils*/}
          <Route path="/facultydetails"
            element={<FacultyDetails userId={userId} />}
          />
          <Route path="/projects-list" element={<ProjectList />} />
          <Route path="/projectsmepart/:userId"
            element={<MyProjectWrapper />}
          />
          <Route path="/student-list" element={<StudentList />} />
          <Route path="/faculty-list" element={<FacultyList />} />
          <Route path="/charts" element={<ProjectDashboard />} />
          <Route path="/myprojects/:userId"
            element={<ProjectWrapper />}
          />
          <Route path="/add-project/:userId"
            element={<AddProjectWrapper />}
          />
          {/* Profile Route */}
          <Route
            path="/profile/:userId"
            element={<ProfileWrapper />}
          />
        </Routes>
      </div>
    </Router>
  );
}

// Wrapper to extract `userId` from URL and pass it to ProfilePage
function ProfileWrapper() {
  const { userId } = useParams();
  return <ProfilePage userId={parseInt(userId, 10)} />;
}
function ProjectWrapper() {
  const { userId } = useParams();
  return <MyProjects userId={parseInt(userId, 10)} />;
}
function AddProjectWrapper() {
  const { userId } = useParams();
  return <AddProject ownerId={parseInt(userId, 10)} />;
}
function MyProjectWrapper() {
  const { userId } = useParams();
  return <UserProjects userId={parseInt(userId, 10)} />;
}
export default App;
