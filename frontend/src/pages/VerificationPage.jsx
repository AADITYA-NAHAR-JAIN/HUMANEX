import React, { useEffect, useState } from "react";
import CameraCapture from "../components/CameraCapture";
import ResultDisplay from "../components/ResultDisplay";
import { verifyUser } from "../services/api";

const VerificationPage = () => {
  const [challenge, setChallenge] = useState("blink");
  const [score, setScore] = useState(null);
  const [loading, setLoading] = useState(false);

  const challenges = ["blink", "move"];

  useEffect(() => {
    const random = challenges[Math.floor(Math.random() * challenges.length)];
    setChallenge(random);
  }, []);

  const handleCapture = async (frames) => {
    console.log("Frame captured:", frames.length);
    setLoading(true);
    const res = await verifyUser(frames, challenge);
    console.log("API response:", res);
    setLoading(false);
    setScore(res.human_score);
  };

  return (
    <div>
      <h1>Multi-frame behavioral verification in progress.</h1>
      <h2>
        {challenge === "blink" ? "Please blink your eyes" : "Move your head slightly"}
      </h2>
      {loading && <p>Verifying human presence...</p>}
      <CameraCapture onCapture={handleCapture} />
      <ResultDisplay score={score} />
    </div>
  );
};

export default VerificationPage;