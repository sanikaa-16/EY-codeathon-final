import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/students': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/students/, '/students') // Optional rewrite
      },
      '/faculty': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/faculty/, '/faculty') // Optional rewrite
      },
      '/faculty_technologies': {
        target: 'http://127.0.0.1:8080', // Replace with your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/faculty_technologies/, '/faculty_technologies')
      },
      '/student_technologies': {
        target: 'http://127.0.0.1:8080', // Replace with your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/student_technologies/, '/student_technologies')
      },
      '/project_students': {
        target: 'http://127.0.0.1:8080', // Replace with your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/project_students/, 'project_students')
      },
      '/project_faculty': {
        target: 'http://127.0.0.1:8080', // Replace with your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/project_faculty/, 'project_faculty')
      },
      '/project_technologies': {
        target: 'http://127.0.0.1:8080', // Replace with your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/project_technologies/, '/project_technologies')
      },
      '/project_themes': {
        target: 'http://127.0.0.1:8080', // Replace with your Flask backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/project_themes/, '/project_themes')
      },
      '/users': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/users/, '/users') // Optional rewrite
      },
      '/departments': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/departments/, '/departments') // Optional rewrite
      },
      '/technologies': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/technologies/, '/technologies') // Optional rewrite
      },
      '/themes': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/themes/, '/themes') // Optional rewrite
      },
      '/projects': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/projects/, '/projects') // Optional rewrite
      },
      '/projectsidname': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/projectsidame/, '/projectsidname') // Optional rewrite
      },
      '/faculty_projects': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/faculty_projects/, '/faculty_projects') // Optional rewrite
      },
      '/student_projects': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/student_projects/, '/student_projects') // Optional rewrite
      },
      '/studentsgetstdid': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/studentsgetstdid/, '/studentsgetstdid') // Optional rewrite
      },
      '/facultyid': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/facultyid/, '/facultyid') // Optional rewrite
      },
    }
  }
});
