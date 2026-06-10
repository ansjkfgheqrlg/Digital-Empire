
import React, { useState, useEffect } from 'react';
import { HashRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import { Navbar } from './components/layout/Navbar';
import { TeamDashboard } from './components/home/TeamDashboard';
import { Footer } from './components/layout/Footer';
import { StarBackground } from './components/ui/StarBackground';
import { Home } from './components/pages/Home';
import { Blog } from './components/pages/Blog';

// Wrapper component to handle scroll-to-top on route change
const ScrollToTop = () => {
  const { pathname } = useLocation();

  useEffect(() => {
    // Only scroll to top if we are not using a hash link
    if (!window.location.hash) {
      window.scrollTo(0, 0);
    }
  }, [pathname]);

  return null;
};

function App() {
  const [isTeamDashboardOpen, setIsTeamDashboardOpen] = useState(false);

  return (
    <Router>
      <div className="min-h-screen bg-transparent text-white overflow-x-hidden relative">
        <ScrollToTop />
        <StarBackground />
        <Navbar />

        <main className="relative">
          <Routes>
            <Route
              path="/"
              element={<Home onOpenSecretDashboard={() => setIsTeamDashboardOpen(true)} />}
            />
            <Route
              path="/blog"
              element={<Blog />}
            />
          </Routes>
        </main>

        <TeamDashboard
          isOpen={isTeamDashboardOpen}
          onClose={() => setIsTeamDashboardOpen(false)}
        />

        <Footer />
      </div>
    </Router>
  );
}

export default App;
