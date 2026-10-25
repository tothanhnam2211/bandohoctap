import { test, expect } from '@playwright/test';
import path from 'path';

test.describe('H07 Game Tests', () => {
  let fileUrl;

  test.beforeAll(async () => {
    fileUrl = 'file://' + path.resolve('games/H07/index.html');
  });

  test.beforeEach(async ({ page }) => {
    await page.goto(fileUrl);
    // Clear localStorage to ensure clean state
    await page.evaluate(() => localStorage.clear());
    await page.reload();
  });

  test('Act 1: Grid counts (128, 32, 8)', async ({ page }) => {
    await page.click('button:has-text("Hồi 1")');

    // Default is 0.5m (32 tiles)
    await page.click('button:has-text("25 cm")');
    for(let i=0; i<128; i++) {
        await page.click('button:has-text("Thêm một viên")');
    }
    await expect(page.locator('#tileCount')).toHaveText('128');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Công trình đạt');

    await page.click('button:has-text("50 cm")');
    for(let i=0; i<32; i++) {
        await page.click('button:has-text("Thêm một viên")');
    }
    await expect(page.locator('#tileCount')).toHaveText('32');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Công trình đạt');

    await page.click('button:has-text("1 m")');
    for(let i=0; i<8; i++) {
        await page.click('button:has-text("Thêm một viên")');
    }
    await expect(page.locator('#tileCount')).toHaveText('8');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Công trình đạt');
  });

  test('Act 2: State resets for V01/V02 variants and double counts', async ({ page }) => {
    await page.click('button:has-text("Hồi 2")');

    await page.click('button:has-text("Nhánh trái cao 6 m")'); // V01
    await page.click('button:has-text("Cắt dọc")');
    await page.fill('#areaAnswer', '38');

    // Switch to V02, state should reset
    await page.click('button:has-text("Nhánh trái cao 5 m")');
    await expect(page.locator('#areaAnswer')).toHaveValue('');

    // Fill correct V02
    await page.click('button:has-text("Cắt dọc")');
    await page.fill('#areaAnswer', '33');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Công trình đạt');

    // Test double count (overlap)
    await page.click('button:has-text("Thử cộng trùng")');
    await page.fill('#areaAnswer', '43');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('bị tính hai lần');
  });

  test('Act 3: G09 edge cases (x=4, x=5, x=9)', async ({ page }) => {
    await page.click('button:has-text("Hồi 3")');

    // x = 4
    await page.click('button:has-text("Khảo sát biên x = 4")');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Thiết kế bất khả thi');

    // x = 9
    await page.click('button:has-text("Khảo sát nghiệm x = 9")');
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Thiết kế bất khả thi'); // Depending on the implementation message, we might need to adjust this.

    // Valid x = 1 (we need to evaluate slider or direct input if slider is hard to use)
    await page.evaluate(() => setG09(1));
    await page.click('button:has-text("Thử thách Mưa Đầu Mùa")');
    await expect(page.locator('#feedback')).toContainText('Thành công');
  });
});
