export const verifyUser = async (frames, challenge) => {
  const res = await fetch("http://127.0.0.1:8000/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ frames, challenge }),
  });

  return res.json();
};