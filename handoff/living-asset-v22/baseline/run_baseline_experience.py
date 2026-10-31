import asyncio
import http.server
import json
import os
import socketserver
import threading
import time
from pathlib import Path
from playwright.async_api import async_playwright

RUNTIME_DIR = Path(r"D:\YOURDREAM.VN\LIVING_ASSET_FACTORY\01_STAGE1_BASELINE_RUNTIME")
SCREENSHOT_DIR = RUNTIME_DIR / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
ARTIFACT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\5d2278ec-09f5-47e5-9e57-a9d76d06c1fa")

PORT = 8765

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(RUNTIME_DIR), **kwargs)
    def log_message(self, format, *args):
        pass

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd

async def run_experience():
    httpd = start_server()
    report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+07:00"),
        "url": f"http://127.0.0.1:{PORT}/nang_suat.html",
        "console_messages": [],
        "page_errors": [],
        "network_failures": [],
        "cdn_resources": [],
        "dependencies_loaded": {},
        "environments_tested": {},
        "problems_tested": [],
        "balance_activity_tests": {},
        "algebra_modes_tested": {},
        "quiz_levels_tested": {},
        "json_io_tested": {},
        "layout_viewports_tested": {},
        "file_protocol_comparison": {}
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--use-gl=angle", "--enable-webgl", "--ignore-gpu-blocklist"])

        # 0. Test file:// protocol first to document difference vs local HTTP server
        page_file = await browser.new_page(viewport={"width": 1440, "height": 900})
        file_errors = []
        page_file.on("console", lambda msg: file_errors.append(f"{msg.type}: {msg.text}") if msg.type in ("error", "warning") else None)
        page_file.on("requestfailed", lambda req: file_errors.append(f"REQ_FAIL: {req.url} ({req.failure})"))
        await page_file.goto(f"file:///{RUNTIME_DIR.as_posix()}/nang_suat.html", wait_until="networkidle")
        await page_file.wait_for_timeout(1000)
        report["file_protocol_comparison"] = {
            "errors_or_warnings": file_errors,
            "json_sidecar_loaded_over_file_protocol": await page_file.evaluate("() => Object.keys(loadedQuestionsByTab)")
        }
        await page_file.close()

        # 1. Main Desktop Experience over HTTP Server (1440x900)
        context = await browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        page = await context.new_page()

        page.on("console", lambda msg: report["console_messages"].append({"type": msg.type, "text": msg.text}))
        page.on("pageerror", lambda err: report["page_errors"].append(str(err)))
        page.on("requestfailed", lambda req: report["network_failures"].append({"url": req.url, "failure": str(req.failure)}))
        page.on("response", lambda res: report["cdn_resources"].append({"url": res.url, "status": res.status}) if ("http" in res.url and "127.0.0.1" not in res.url) or res.url.endswith(".json") else None)

        await page.goto(f"http://127.0.0.1:{PORT}/nang_suat.html", wait_until="networkidle")
        await page.wait_for_timeout(1500)

        # Verify loaded dependencies
        report["dependencies_loaded"] = await page.evaluate("""() => ({
            THREE: typeof window.THREE !== 'undefined' ? window.THREE.REVISION : false,
            OrbitControls: typeof window.THREE !== 'undefined' && typeof window.THREE.OrbitControls === 'function',
            MathJax: typeof window.MathJax !== 'undefined' && typeof window.MathJax.typesetPromise === 'function',
            Chart: typeof window.Chart !== 'undefined' ? window.Chart.version || true : false,
            Matter: typeof window.Matter !== 'undefined' ? window.Matter.version || true : false,
            MatterUsedInCode: document.documentElement.innerHTML.split('Matter').length - 1,
            WebGLContextOk: !!renderer && !!renderer.getContext(),
            JSONSidecarTabsLoaded: Object.keys(loadedQuestionsByTab)
        })""")

        # --- ENVIRONMENT 1: FLEET AND CARGO DISTRIBUTION ---
        await page.screenshot(path=str(SCREENSHOT_DIR / "env1_initial_desktop.png"))
        env1_initial = await page.evaluate("""() => ({
            dataState: JSON.parse(JSON.stringify(dataState[1])),
            truckCount: truckObjects.length,
            plannedTrucks: truckObjects.filter(t => !t.isExtra).length,
            extraTrucks: truckObjects.filter(t => t.isExtra).length,
            telemetryText: document.getElementById('telemetry-display').innerText,
            algebraText: document.getElementById('algebra-display').innerText,
            hudPlanText: document.getElementById('fleet-plan-rate')?.innerText,
            hudActualText: document.getElementById('fleet-actual-rate')?.innerText,
            hudPlanStatus: document.getElementById('fleet-plan-status')?.innerText,
            hudActualStatus: document.getElementById('fleet-actual-status')?.innerText
        })""")

        # Start simulation, capture mid-flight, pause, then finish
        await page.click("#btn-play")
        await page.wait_for_timeout(900)
        await page.click("#btn-pause")
        env1_mid_sim = await page.evaluate("""() => ({
            simProgress: simProgress,
            isSimRunning: isSimRunning,
            visibleParcels: truckObjects.filter(t => t.parcel && t.parcel.visible).length,
            warehouseScaleY: warehouseBoxMesh ? warehouseBoxMesh.scale.y : null,
            sampleTruckLoads: truckObjects.slice(0, 4).map(t => Number(t.currentLoad.toFixed(2)))
        })""")
        await page.screenshot(path=str(SCREENSHOT_DIR / "env1_mid_simulation.png"))

        # Fast-forward to completion
        await page.evaluate("() => { simProgress = 0.995; startSimulation(); }")
        await page.wait_for_timeout(300)
        env1_completed = await page.evaluate("""() => ({
            simProgress: simProgress,
            bannerVisible: document.getElementById('banner-alert').style.display !== 'none',
            bannerText: document.getElementById('banner-alert').innerText,
            finalTruckLoads: truckObjects.map(t => Number(t.currentLoad.toFixed(2)))
        })""")
        await page.screenshot(path=str(SCREENSHOT_DIR / "env1_completed.png"))

        # Test parameter changes & boundary configurations in Env 1
        # Boundary 1: Set k = 5, x = 18 -> check clamping x <= 20 - k = 15
        await page.evaluate("() => { updateParam(1, 'x', 18); updateParam(1, 'k', 5); }")
        env1_boundary_clamp = await page.evaluate("""() => ({
            x_after_k5: dataState[1].x,
            k: dataState[1].k,
            slider_x_max: document.getElementById('slider-x').max,
            total_trucks_in_3d: truckObjects.length
        })""")

        # Boundary 2: Non-divisible Q=60, x=11, k=3 -> check decimal approximation and mutation of problem statement
        await page.evaluate("() => { updateParam(1, 'Q', 60); updateParam(1, 'k', 3); updateParam(1, 'x', 11); }")
        await page.wait_for_timeout(200)
        env1_non_divisible = await page.evaluate("""() => ({
            Q: dataState[1].Q,
            x: dataState[1].x,
            k: dataState[1].k,
            stored_delta_m: dataState[1].delta_m,
            problemStatementText: document.getElementById('problem-statement-content').innerText,
            algebraText: document.getElementById('algebra-display').innerText
        })""")

        # Capacity C constraint test
        await page.evaluate("() => { selectProblemById('VD5_Tr117'); adjustTruckCapacityC(-1.0); }")
        env1_capacity_test = await page.evaluate("""() => ({
            C: dataState[1].C,
            planStatus: document.getElementById('fleet-plan-status').innerText,
            actualStatus: document.getElementById('fleet-actual-status').innerText
        })""")

        report["environments_tested"]["env1_fleet"] = {
            "initial": env1_initial,
            "mid_sim": env1_mid_sim,
            "completed": env1_completed,
            "boundary_clamp": env1_boundary_clamp,
            "non_divisible_mutation_test": env1_non_divisible,
            "capacity_constraint_test": env1_capacity_test
        }

        # --- BALANCE REASONING ACTIVITY TEST ---
        await page.evaluate("() => { selectProblemById('VD5_Tr117'); }")
        await page.click("#btn-open-balance-hud")
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(SCREENSHOT_DIR / "balance_step1_open.png"))

        # Deliberately test WRONG choice in Step 1 ('right' -> actual is heavier)
        await page.click("#btn-step1-right")
        bal_step1_wrong = await page.evaluate("""() => ({
            step1Choice: balanceState.step1Choice,
            feedbackText: document.getElementById('balance-step1-feedback').innerText,
            step2Visible: document.getElementById('bal-step2-box').style.display !== 'none'
        })""")

        # Now select CORRECT choice in Step 1 ('left' -> plan is heavier)
        await page.click("#btn-step1-left")
        await page.wait_for_timeout(300)
        bal_step1_right = await page.evaluate("""() => ({
            step1Choice: balanceState.step1Choice,
            step1Collapsed: document.getElementById('bal-step1-collapsed').style.display !== 'none',
            step2Visible: document.getElementById('bal-step2-box').style.display !== 'none'
        })""")

        # Step 2: Deliberately place weight on WRONG pan (heavier pan 'plan')
        await page.click("#btn-place-plan")
        await page.wait_for_timeout(300)
        bal_step2_wrong = await page.evaluate("""() => ({
            beamClass: document.getElementById('balance-beam').className,
            feedbackText: document.getElementById('balance-step2-feedback').innerText,
            liveRelation: document.getElementById('balance-live-relation').innerText,
            step3Visible: document.getElementById('bal-step3-box').style.display !== 'none'
        })""")
        await page.screenshot(path=str(SCREENSHOT_DIR / "balance_step2_wrong_pan.png"))

        # Step 2: Place weight on CORRECT pan ('actual')
        await page.click("#btn-place-actual")
        await page.wait_for_timeout(400)
        bal_step2_correct = await page.evaluate("""() => ({
            beamClass: document.getElementById('balance-beam').className,
            relSign: document.getElementById('balance-rel-sign').innerText,
            liveRelation: document.getElementById('balance-live-relation').innerText,
            step3Visible: document.getElementById('bal-step3-box').style.display !== 'none',
            symEqText: document.getElementById('bal-step3-card-sym').innerText,
            numEqText: document.getElementById('bal-step3-card-num').innerText
        })""")
        await page.screenshot(path=str(SCREENSHOT_DIR / "balance_step3_unlocked.png"))

        # Swap sides test
        await page.click("#btn-swap-sides")
        bal_swapped = await page.evaluate("""() => ({
            swapped: balanceState.swapped,
            liveRelation: document.getElementById('balance-live-relation').innerText
        })""")
        await page.click("#btn-close-balance")

        report["balance_activity_tests"] = {
            "step1_wrong": bal_step1_wrong,
            "step1_correct": bal_step1_right,
            "step2_wrong_pan": bal_step2_wrong,
            "step2_correct_balanced": bal_step2_correct,
            "swapped_sides": bal_swapped
        }

        # --- ENVIRONMENT 2: GARMENT PRODUCTION ---
        await page.click("#tab-btn-2")
        await page.wait_for_timeout(500)
        await page.evaluate("() => { simProgress = 0.6; updateAlgebraPanel(); }")
        await page.wait_for_timeout(300)
        await page.screenshot(path=str(SCREENSHOT_DIR / "env2_garment_production.png"))
        await page.evaluate("() => { simProgress = 0.995; startSimulation(); }")
        await page.wait_for_timeout(300)
        env2_data = await page.evaluate("""() => ({
            dataState: JSON.parse(JSON.stringify(dataState[2])),
            sewingObjectsCount: sewingObjects.length,
            planLaneItems: sewingObjects.filter(o => o.lane === 'plan').length,
            actualLaneItems: sewingObjects.filter(o => o.lane === 'actual').length,
            hudPlanRate: document.getElementById('hud-plan-rate')?.innerText,
            hudActualRate: document.getElementById('hud-actual-rate')?.innerText,
            hudPlanCount: document.getElementById('hud-plan-count')?.innerText,
            hudActualCount: document.getElementById('hud-actual-count')?.innerText,
            bannerText: document.getElementById('banner-alert').innerText,
            telemetryText: document.getElementById('telemetry-display').innerText
        })""")
        report["environments_tested"]["env2_garment"] = env2_data

        # --- ENVIRONMENT 3: TREE PLANTING ---
        await page.click("#tab-btn-3")
        await page.wait_for_timeout(500)
        await page.evaluate("() => { simProgress = 0.995; startSimulation(); }")
        await page.wait_for_timeout(300)
        await page.screenshot(path=str(SCREENSHOT_DIR / "env3_tree_planting.png"))
        env3_data = await page.evaluate("""() => ({
            dataState: JSON.parse(JSON.stringify(dataState[3])),
            treeMeshesCount: treeMeshes.length,
            absentBadgesCount: Array.from(document.querySelectorAll('.truck-num-badge.extra-truck')).length,
            presentBadgesCount: Array.from(document.querySelectorAll('.truck-num-badge:not(.extra-truck)')).length,
            hudPlanRate: document.getElementById('fleet-plan-rate')?.innerText,
            hudActualRate: document.getElementById('fleet-actual-rate')?.innerText,
            bannerText: document.getElementById('banner-alert').innerText,
            telemetryText: document.getElementById('telemetry-display').innerText
        })""")
        report["environments_tested"]["env3_trees"] = env3_data

        # --- ENVIRONMENT 4: TWO-STAGE PRODUCTIVITY ---
        await page.click("#tab-btn-4")
        await page.wait_for_timeout(500)
        await page.evaluate("() => { simProgress = 0.65; startSimulation(); }")
        await page.wait_for_timeout(400)
        await page.click("#btn-pause")
        await page.screenshot(path=str(SCREENSHOT_DIR / "env4_two_stage.png"))
        await page.evaluate("() => { simProgress = 0.995; startSimulation(); }")
        await page.wait_for_timeout(300)
        env4_data = await page.evaluate("""() => ({
            dataState: JSON.parse(JSON.stringify(dataState[4])),
            sewingObjectsCount: sewingObjects.length,
            hudPlanRate: document.getElementById('hud-plan-rate')?.innerText,
            hudActualRate: document.getElementById('hud-actual-rate')?.innerText,
            hudPlanCount: document.getElementById('hud-plan-count')?.innerText,
            hudActualCount: document.getElementById('hud-actual-count')?.innerText,
            bannerText: document.getElementById('banner-alert').innerText,
            telemetryText: document.getElementById('telemetry-display').innerText
        })""")
        report["environments_tested"]["env4_two_stage"] = env4_data

        # --- TEST ALL 9 EXERCISES & 1VAR/2VAR ALGEBRA MODES ---
        problem_ids = await page.evaluate("() => Object.keys(problemCatalog)")
        for pid in problem_ids:
            p_info = await page.evaluate(f"""(pid) => {{
                selectProblemById(pid);
                setAlgebraSolveMode('1var');
                const eq1 = document.getElementById('algebra-display').innerText;
                setAlgebraSolveMode('2var');
                const eq2 = document.getElementById('algebra-display').innerText;
                setAlgebraSolveMode('1var');
                return {{
                    id: pid,
                    tab: currentTab,
                    params: JSON.parse(JSON.stringify(dataState[currentTab])),
                    problemText: document.getElementById('problem-statement-content').innerText,
                    eq1var_preview: eq1.replace(/\\s+/g, ' ').slice(0, 180),
                    eq2var_preview: eq2.replace(/\\s+/g, ' ').slice(0, 180)
                }};
            }}""", pid)
            report["problems_tested"].append(p_info)

        # --- TEST 4 LEVELS OF DIFFERENTIATED QUIZ ---
        await page.evaluate("() => selectProblemById('VD5_Tr117')")
        for lvl in ["NB", "TH", "VD", "VDNC"]:
            q_res = await page.evaluate(f"""(lvl) => {{
                switchQuizLevel(lvl);
                const qText = document.getElementById('quiz-question-box').innerText;
                const opts = Array.from(document.querySelectorAll('.quiz-opt-btn')).map(b => b.innerText);
                answerScaffoldingQuiz(1); // Deliberately wrong first
                const wrongExp = document.getElementById('quiz-explain-box').innerText;
                answerScaffoldingQuiz(0); // Correct answer (Wait: is index 0 ALWAYS correct?!)
                const rightExp = document.getElementById('quiz-explain-box').innerText;
                return {{
                    level: lvl,
                    question: qText,
                    optionsCount: opts.length,
                    wrongFeedbackPreview: wrongExp.slice(0, 100),
                    rightFeedbackPreview: rightExp.slice(0, 100)
                }};
            }}""", lvl)
            report["quiz_levels_tested"][lvl] = q_res

        # Check whether correct answer index is hardcoded to 0 across all tabs and levels!
        report["quiz_levels_tested"]["all_correct_indices_audit"] = await page.evaluate("""() => {
            const audit = {};
            [1, 2, 3, 4].forEach(t => {
                switchTab(t);
                const bank = buildQuizBankForCurrentState();
                audit['tab_' + t] = Object.fromEntries(Object.entries(bank).map(([k, v]) => [k, v.correct]));
            });
            return audit;
        }""")

        # --- TEST JSON IMPORT / EXPORT ---
        json_test = await page.evaluate("""() => {
            const customPayload = {
                id: "Custom_Test_01",
                tab: 1,
                badge: "Test Import",
                title: "[Custom_Test_01] Đội xe chở 90 tấn, thêm 3 xe, giảm 1.5 tấn/xe",
                params: { Q: 90, x: 12, k: 3, delta_m: 1.5, C: 6.0 },
                questionTarget: "Tính số xe ban đầu?"
            };
            applyLoadedJSONData(customPayload, true);
            return {
                activeProblemId: activeProblemId,
                dataState1: JSON.parse(JSON.stringify(dataState[1])),
                selectorOptionsCount: document.getElementById('problem-selector').options.length
            };
        }""")
        report["json_io_tested"] = json_test

        # --- TEST TABLET & MOBILE VIEWPORTS (1024x768 Landscape & 768x1024 Portrait) ---
        await page.evaluate("() => selectProblemById('VD5_Tr117')")
        for vp_name, w, h in [("tablet_landscape_1024x768", 1024, 768), ("tablet_portrait_768x1024", 768, 1024)]:
            await page.set_viewport_size({"width": w, "height": h})
            await page.wait_for_timeout(400)
            await page.screenshot(path=str(SCREENSHOT_DIR / f"layout_{vp_name}.png"))
            vp_metrics = await page.evaluate("""() => {
                const sb = document.getElementById('sidebar').getBoundingClientRect();
                const cv = document.getElementById('canvas-container').getBoundingClientRect();
                const hp = document.getElementById('fleet-plan-title')?.parentElement?.parentElement?.getBoundingClientRect();
                const ha = document.getElementById('fleet-actual-title')?.parentElement?.parentElement?.getBoundingClientRect();
                return {
                    sidebarWidth: sb.width,
                    canvasWidth: cv.width,
                    canvasHeight: cv.height,
                    canvasRatioOfScreen: Number((cv.width / window.innerWidth).toFixed(2)),
                    hudPlanRect: hp ? { left: Math.round(hp.left), right: Math.round(hp.right), top: Math.round(hp.top), width: Math.round(hp.width) } : null,
                    hudActualRect: ha ? { left: Math.round(ha.left), right: Math.round(ha.right), top: Math.round(ha.top), width: Math.round(ha.width) } : null,
                    hudOverlapOrClipped: (hp && ha) ? (hp.right > ha.left || ha.right > window.innerWidth || hp.left < sb.right) : null
                };
            }""")
            report["layout_viewports_tested"][vp_name] = vp_metrics

        await browser.close()

    httpd.shutdown()
    out_path = RUNTIME_DIR / "STAGE1_RUNTIME_EXPERIENCE_LOG.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Saved runtime report to:", out_path)

if __name__ == "__main__":
    asyncio.run(run_experience())
