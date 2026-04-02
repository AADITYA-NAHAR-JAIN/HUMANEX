import React from "react";

const ResultDisplay = ({ score }) => {
  if (score === null) return <p>No result yet</p>;

  return (
    <div>
      <h2 style={{ color: score > 80 ? "green" : "red" }}>
        {score > 80 ? "Human Verified ✅" : "Suspicious ❌"}
      </h2>
      <p>Score: {score}</p>
    </div>
  );
};

export default ResultDisplay;