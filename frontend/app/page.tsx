"use client";

import { useState } from "react";

export default function Home() {
  const [topic, setTopic] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function research() {
    setLoading(true);

    const response = await fetch(
      `http://localhost:8000/research?topic=${encodeURIComponent(topic)}`
    );

    const data = await response.json();

    setAnswer(data.answer);
    setLoading(false);
  }

  return (
    <main className="min-h-screen p-10">
      <h1 className="text-4xl font-bold">
        AI Research Assistant
      </h1>

      <input
        className="mt-8 w-full border p-3"
        placeholder="What do you want to research?"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button
        className="mt-4 rounded bg-black px-5 py-3 text-white"
        onClick={research}
      >
        {loading ? "Researching..." : "Research"}
      </button>

      {answer && (
        <div className="mt-8">
          <h2 className="text-2xl font-bold">Answer</h2>
          <p className="mt-3 whitespace-pre-line">{answer}</p>
        </div>
      )}
    </main>
  );
}
