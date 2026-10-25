import { test, expect } from '@playwright/test';
import path from 'path';

test('H07 mobile layout stays within viewport across three acts', async ({ page }, testInfo) => {
  await page.goto('file://' + path.resolve('games/H07/index.html'));
  await page.evaluate(() => localStorage.clear());
  await page.reload();

  for (const act of [1, 2, 3]) {
    await page.getByRole('button', { name: new RegExp('Hồi ' + act) }).first().click();
    await expect(page.locator('#stage')).toBeVisible();
    const geometry = await page.evaluate(() => ({
      viewport: document.documentElement.clientWidth,
      document: document.documentElement.scrollWidth,
      canvas: document.querySelector('#stage').getBoundingClientRect().toJSON(),
    }));
    expect(geometry.document, 'horizontal overflow in act ' + act).toBeLessThanOrEqual(geometry.viewport + 1);
    expect(geometry.canvas.width, 'canvas too narrow in act ' + act).toBeGreaterThan(250);
    await page.screenshot({ path: testInfo.outputPath('h07-mobile-act-' + act + '.png'), fullPage: true });
  }
});
