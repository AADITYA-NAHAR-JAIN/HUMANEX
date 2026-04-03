export const verifyUser = async (frames, challenge) => {
  const res = await fetch("https//:humanex.onrender.com/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ frames, challenge }),
  });

  return res.json();
};