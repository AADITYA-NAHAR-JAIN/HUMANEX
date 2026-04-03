export const verifyUser = async (frames, challenge) => {
  const res = await fetch("https://humanex.onrender.com/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ frames, challenge }),
  });

  if (!res.ok) {
    throw new Error("API request failed");
  }

  return await res.json();
};