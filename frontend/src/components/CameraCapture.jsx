import React, { useRef, useEffect } from "react";

const CameraCapture = ({ onCapture }) => {
  const videoRef = useRef(null);

  useEffect(() => {
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
      })
      .catch((err) => console.error(err));
  }, []);

  const captureFrames = async () => {
  let frames = [];

  for (let i = 0; i < 8; i++) {
    const canvas = document.createElement("canvas");
    if (!videoRef.current) return;
    canvas.width = videoRef.current.videoWidth || 400;
    canvas.height = videoRef.current.videoHeight || 300;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(videoRef.current, 0, 0);

    frames.push(canvas.toDataURL("image/jpeg"));

    await new Promise(r => setTimeout(r, 500));
  }

  onCapture(frames);
};

  return (
    <div>
      <video ref={videoRef} autoPlay playsInline width="400" />
      <button onClick={captureFrames}>Verify</button>
    </div>
  );
};

export default CameraCapture;