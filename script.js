// Emergency
const emergencyInput = document.getElementById("emergencyInput");
const locationInput = document.getElementById("locationInput");
const addEmergencyBtn = document.getElementById("addEmergencyBtn");
const emergencyList = document.getElementById("emergencyList");

async function fetchEmergencies() {
  const res = await fetch("http://localhost:5000/emergencies");
  const data = await res.json();
  emergencyList.innerHTML = "";
  data.forEach(e => {
    const li = document.createElement("li");
    li.textContent = `${e.message} - Location: ${e.location}`;
    emergencyList.appendChild(li);
  });
}

addEmergencyBtn.addEventListener("click", async () => {
  await fetch("http://localhost:5000/emergency", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: emergencyInput.value,
      location: locationInput.value
    })
  });
  emergencyInput.value = "";
  locationInput.value = "";
  fetchEmergencies();
});

// Medication
const medName = document.getElementById("medName");
const medTime = document.getElementById("medTime");
const addMedBtn = document.getElementById("addMedBtn");
const medList = document.getElementById("medList");

async function fetchMeds() {
  const res = await fetch("http://localhost:5000/medications");
  const data = await res.json();
  medList.innerHTML = "";
  data.forEach(m => {
    const li = document.createElement("li");
    li.textContent = `${m.name} at ${m.time}`;
    medList.appendChild(li);
  });
}

addMedBtn.addEventListener("click", async () => {
  await fetch("http://localhost:5000/medication", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: medName.value,
      time: medTime.value
    })
  });
  medName.value = "";
  medTime.value = "";
  fetchMeds();
});

// Chatbot
const chatInput = document.getElementById("chatInput");
const chatBtn = document.getElementById("chatBtn");
const chatResult = document.getElementById("chatResult");

chatBtn.addEventListener("click", async () => {
  const res = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: chatInput.value })
  });
  const data = await res.json();
  chatResult.innerHTML = "";
  for (const symptom in data) {
    const div = document.createElement("div");
    div.textContent = `${symptom}: ${data[symptom].join(", ")}`;
    chatResult.appendChild(div);
  }
  chatInput.value = "";
});
