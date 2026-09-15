function runLab(name) {
  let out = document.getElementById("output");
  if(name == "Confidentiality"){
    out.innerHTML = "Confidentiality: Encrypting data... SUCCESS! Data Encrypted. Hackers can't read it.";
  }
  if(name == "Integrity"){
    out.innerHTML = "Integrity: Checking SHA256 hash... MATCH - Data is clean, not tampered.";
  }
  if(name == "Availability"){
    out.innerHTML = "Availability: Attack detected! Restoring from backup... RESTORED - Zero downtime!";
  }
}
