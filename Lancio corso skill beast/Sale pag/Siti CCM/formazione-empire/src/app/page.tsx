import ShellHeader from "@/components/shell-header";
import ShellFooter from "@/components/shell-footer";
import LandingHero from "@/components/sections/landing-hero";
import LandingCourses from "@/components/sections/landing-courses";
import LandingMethod from "@/components/sections/landing-method";
import LandingFaq from "@/components/sections/landing-faq";
import LandingFinalCta from "@/components/sections/landing-final-cta";

export default function Home() {
  return (
    <>
      <ShellHeader variant="public" />
      <main>
        <LandingHero />
        <LandingCourses />
        <LandingMethod />
        <LandingFaq />
        <LandingFinalCta />
      </main>
      <ShellFooter />
    </>
  );
}
