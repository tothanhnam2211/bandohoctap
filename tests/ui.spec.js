const { test, expect } = require('@playwright/test');

test('TextNote interactive renders and interactions work for a generic loaded lesson', async ({ page }) => {
  await page.goto('http://localhost:3000/?nocache=' + Date.now());

  // Wait for the list to be visible
  const curriculumList = page.locator('#curriculum-list');
  await curriculumList.waitFor({ state: 'visible' });

  // The textnote was appended as day 46
  await page.evaluate(async () => {
    if (window.loadDay) await window.loadDay(46);
  });
  await page.waitForTimeout(1000);

  // Make sure tab content is visible
  const textnoteTab = page.locator('#tab-textnote');
  await page.evaluate(() => {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
    document.getElementById('tab-textnote').classList.remove('hidden');
  });
  await expect(textnoteTab).toBeVisible();

  // Explicitly wait for fetch to complete by waiting for title to update
  await expect(page.locator('#textnote-title-text')).not.toHaveText('Đang tải...', { timeout: 10000 });

  // Test Worked Example (Reveal steps)
  const nextBtn = page.getByText(/Suy nghĩ & Mở bước/);
  await expect(nextBtn).toBeVisible();
  await nextBtn.click();
  // Step 1 should be visible
  await expect(page.locator('#tn-step-0')).toBeVisible();

  // Test Math Expression Check (Correct)
  const input2a = page.locator('#tn-ex-2a');
  await input2a.fill('26');
  await page.locator('button:has-text("Kiểm tra")').first().click();
  const feedback2a = page.locator('#tn-fb-2a');
  await expect(feedback2a).toContainText('Chính xác');

  // Test Paper Mode click
  page.on('dialog', dialog => dialog.accept());
  await page.locator('#textnote-paper-mode').click();
});
