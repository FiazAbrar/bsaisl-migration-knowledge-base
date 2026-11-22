# Meta / WhatsApp setup (test account)

Checked against Meta's docs on 17 Nov 2026. Meta renames buttons often; if a label differs, look for the closest match.
Paste every value into `navigator-bot/.env`, never into chat or git.

## Part A: Developer account (once)

1. Open https://developers.facebook.com and click **Log in** (use your Facebook account).
2. Click **Get Started** (or open https://developers.facebook.com/async/registration/).
3. Accept the terms, verify your phone number and email when asked, choose your role (e.g. **Developer**), click **Complete registration**.

## Part B: Create the app

1. Open https://developers.facebook.com/apps and click **Create App**.
2. **App details:** App name `Navigator Bot Test`, your email. Click **Next**.
3. **Use case:** select **Connect with customers through WhatsApp**. Click **Next**.
4. **Business:** choose **Create a business portfolio** (name e.g. `Navigator Test`, your name and email), or pick an existing one. Click **Next**.
5. **Requirements:** probably none listed. Click **Next**.
6. **Overview:** check the details and click **Create app**. Enter your Facebook password if asked.

You land on the app **Dashboard**. Click **Customize the Connect with customers through WhatsApp use case**.
This opens **Use cases > Customize > Connect on WhatsApp**. Since late 2026 its menu reads **Overview / Basic setup (Step 1. Try it out, Step 2. Production setup, Step 3. Business verification)**; older layouts show **Quickstart / API Setup / Configuration**.
Keep **Integrate with API** selected (not "Become a Partner").

## Part C: Test number and first message

1. Click **Step 1. Try it out** (older layout: **Start using the API** or **API Setup**).
2. Under **API Setup**, connect a Messaging account:
   - If one was created with the portfolio, it is already selected; check it.
   - Otherwise click **Create a WhatsApp Business account** and follow the prompts.
3. Copy the **Messaging account ID** (also called WhatsApp Business Account ID) to `WHATSAPP_BUSINESS_ACCOUNT_ID`.
4. Click **Generate access token**, log in and click **Continue** on the permission pop-ups. This token expires within hours; it's only for this test.
5. **From:** keep the test number Meta gives you (a +1 555 number). Copy the **Phone number ID** shown under it to `WHATSAPP_PHONE_NUMBER_ID`.
6. **To:** click the dropdown, **Manage phone number list**, add your own WhatsApp number with country code (+880...), enter the 5-digit code WhatsApp sends you.
   Put the same number in `TEST_RECIPIENT` as `8801XXXXXXXXX` (no +).
7. Click **Send message**. You receive a "Hello World" message on WhatsApp (can take a minute).
8. **Reply to it** with anything (e.g. "hi"). This opens the 24-hour window that lets the bot answer you.
9. Save the test number as a contact on your phone, so you can find the chat later.

## Part D: App secret

1. Left menu: **App settings > Basic**.
2. Next to **App secret**, click **Show**, enter your password, copy it to `META_APP_SECRET`.

## Part E: Permanent token (System User)

1. Open https://business.facebook.com/latest/settings and check the portfolio from Part B is selected (top-left).
2. Left menu: **Users > System users**. Click **+ Add**.
   - Name: `navigator-bot`, Role: **Admin**. Click **Create system user**.
3. Click the new system user, then **Assign assets**:
   - **Apps** > your app > turn on **Manage app** (Full control).
   - **WhatsApp accounts** > your account > turn on **Manage WhatsApp Business accounts** (Full control).
   - If a **Messaging accounts** tab is shown, give full control there too.
   - Click **Assign assets**. Reload the page after a minute and check both assets appear.
4. Click **Generate token**:
   - App: your app.
   - Expiration: **Never**.
   - Permissions (search "business"): tick `business_management`, `whatsapp_business_management`, `whatsapp_business_messaging`.
   - Click **Generate token**. Copy it at once to `WHATSAPP_ACCESS_TOKEN` (it is shown only once).

## Part F: Verify token

Make up a long random string (e.g. 30 letters and digits) and put it in `WHATSAPP_VERIFY_TOKEN`. You type the same string into Meta in Part H.

## Part G: ngrok (public HTTPS address for your PC)

1. In a terminal: `winget install ngrok.ngrok`, then `ngrok update` (winget installs 3.3.1; ngrok accounts now require 3.29 or newer).
2. Sign up at https://dashboard.ngrok.com/signup.
3. Dashboard > **Your Authtoken** > copy, then run `ngrok config add-authtoken <token>`.
4. Dashboard > **Domains** > **+ New Domain** (one free static domain). Copy it (e.g. `abc-def.ngrok-free.app`) to `PUBLIC_DOMAIN`.

## Part H: Webhook (after the bot is built and running)

The bot must be running behind ngrok at this moment, because Meta calls it while you save.

1. **Use cases > Customize > Connect on WhatsApp > Step 2. Production setup**, webhook part only (older layout: **Configuration**). Don't add your own phone number there; the test number is enough. Skip **Step 3. Business verification**; BRAC IT does that on its own account.
2. Under **Webhook**, click **Edit**:
   - Callback URL: `https://<PUBLIC_DOMAIN>/webhook`
   - Verify token: the value of `WHATSAPP_VERIFY_TOKEN`
   - Click **Verify and save**.
3. Under **Webhook fields**, click **Manage**, find **messages**, click **Subscribe**. Close.
4. **Link the app to the WhatsApp account** (the dashboard skips this on some new accounts; without it, messages go to Meta's sample app instead of yours):
   `curl -X POST "https://graph.facebook.com/v27.0/<WHATSAPP_BUSINESS_ACCOUNT_ID>/subscribed_apps" -H "Authorization: Bearer <WHATSAPP_ACCESS_TOKEN>"`
   Check with the same URL as a GET: your app's name must be in the list.
5. **Publish the app** (left menu **Publish**). While the app is unpublished, Meta only delivers the dashboard's test webhooks, not real messages, even from you. Publishing asks for a **Privacy Policy URL** (any public page describing what the bot stores), an **app icon** and a **category**. No App Review is needed for your own WhatsApp account.
6. Send a message from your phone to the test number; the bot should answer.

## If something fails

- **Error code 200 / permission error:** the system user is missing an asset (Part E step 3) or a permission (step 4). Fix and generate a new token.
- **"Recipient phone number not in allowed list":** add the number in Part C step 6.
- **Bot gets no messages:** check Part H step 3 (subscribed to messages), that ngrok is running with your static domain, and that you messaged the test number in the last 24 hours. If it still fails, the app may need to be switched to **Live** mode (top of dashboard), which asks for a privacy-policy URL.
- **Token expired:** you are still using the token from Part C step 4; use the System User token from Part E.
