/**
 * Every fixed message the bot sends, in English and Bangla. AI answers follow the person's own language
 * and script (prompts/system.md); these fixed texts go by the script of their message: Bangla script gets
 * Bangla, anything else English. `*text*` is bold; each channel converts it to its own format.
 */

import type { RefusalReason } from "../guard/guard.ts";
import { MAX_CHARS } from "../guard/guard.ts";

export type Lang = "en" | "bn";

/** Bangla script anywhere in the message means Bangla. */
export function detectLang(text: string): Lang {
  return /[ঀ-৿]/.test(text) ? "bn" : "en";
}

const BN_DIGITS = "০১২৩৪৫৬৭৮৯";
export function bnDigits(n: number | string): string {
  return String(n).replace(/\d/g, (d) => BN_DIGITS[Number(d)] ?? d);
}

export const HELP_LINE: Record<Lang, string> = {
  en: "For urgent help, call 16135 (free from Bangladesh) or +880 9610102030 from abroad.",
  bn: "জরুরি সাহায্যের জন্য ফোন করুন 16135 (বাংলাদেশ থেকে বিনামূল্যে), বিদেশ থেকে +880 9610102030।",
};

interface Messages {
  welcome: (countries: string) => string;
  privacy: (link: string | undefined) => string;
  deleted: string;
  reset: string;
  whichCountry: (countries: string) => string;
  testMode: string;
  guideChosen: (guide: string) => string;
  noMatch: (guide: string) => string;
  closest: (guide: string) => string;
  sendText: string;
  tooLong: string;
  personalRemoved: string;
  error: string;
  refusal: Record<RefusalReason, string>;
}

export const MESSAGES: Record<Lang, Messages> = {
  en: {
    welcome: (countries) =>
      "Hello! I answer questions about going abroad to work, from BRAC's guides for Bangladeshi workers.\n" +
      `I have guides for: ${countries}.\n` +
      "Tell me the country, then ask your question, for example: *Saudi Arabia*, then *medical check cost*.\n" +
      "Send *reset* to start over, or *delete my data* to erase your history.",
    privacy: (link) =>
      "Privacy: to help you next time, I keep a short note about your situation for 12 months after your last " +
      "message, and our messages for 90 days. Never send your NID, passport or bank details. " +
      `Send *delete my data* at any time to erase everything.${link ? ` More: ${link}` : ""}`,
    deleted: "Your conversation history with this bot has been deleted.",
    reset: "OK, let's start again. Which country are you asking about?",
    whichCountry: (countries) => `Which country are you asking about? I have guides for: ${countries}.`,
    testMode: "(Test mode: AI answers are not connected yet.)",
    guideChosen: (guide) => `OK, the *${guide}* guide. What would you like to know?`,
    noMatch: (guide) =>
      `Guide: *${guide}*. I couldn't find a section that matches your words. Try other words, or English keywords.`,
    closest: (guide) => `Closest sections in the *${guide}* guide:`,
    sendText: "Please send your question as a text message.",
    tooLong: `Please send a shorter question, under ${MAX_CHARS} characters.`,
    personalRemoved:
      "For your safety, I removed what looked like an ID, passport, card or phone number from your message. Never share these in a chat.",
    error: "Sorry, something went wrong. Please try again in a minute.",
    refusal: {
      minute: "You're sending messages very fast. Please wait a minute, then ask again.",
      day: `You've reached today's limit of questions. Please come back tomorrow. ${HELP_LINE.en}`,
      ip: `Too many questions are coming from your network today. Please try again tomorrow. ${HELP_LINE.en}`,
      sessions: `Too many new chats are coming from your network. Please try again in an hour. ${HELP_LINE.en}`,
      budget: `The Navigator is very busy today. Please try again tomorrow. ${HELP_LINE.en}`,
      busy: `The Navigator is very busy right now. Please try again in a minute. ${HELP_LINE.en}`,
    },
  },
  bn: {
    welcome: (countries) =>
      "হ্যালো! বিদেশে কাজে যাওয়া নিয়ে আপনার প্রশ্নের উত্তর দিই, বাংলাদেশি কর্মীদের জন্য ব্র্যাকের গাইড থেকে।\n" +
      `যেসব দেশের গাইড আছে: ${countries}।\n` +
      "প্রথমে দেশের নাম লিখুন, তারপর প্রশ্ন করুন, যেমন: *সৌদি আরব*, তারপর *মেডিকেলের খরচ*।\n" +
      "নতুন করে শুরু করতে *reset* লিখুন, আর আপনার সব তথ্য মুছতে *আমার তথ্য মুছে দিন* লিখুন।",
    privacy: (link) =>
      "গোপনীয়তা: পরের বার সাহায্য করতে আপনার অবস্থা নিয়ে একটি ছোট নোট আপনার শেষ বার্তার পর ১২ মাস, " +
      "আর আমাদের বার্তাগুলো ৯০ দিন রাখা হয়। কখনো আপনার এনআইডি, পাসপোর্ট বা ব্যাংকের তথ্য পাঠাবেন না। " +
      `সব মুছতে যেকোনো সময় *আমার তথ্য মুছে দিন* লিখুন।${link ? ` বিস্তারিত: ${link}` : ""}`,
    deleted: "এই বটের সঙ্গে আপনার কথোপকথন ও তথ্য মুছে ফেলা হয়েছে।",
    reset: "ঠিক আছে, নতুন করে শুরু করি। কোন দেশ নিয়ে জানতে চান?",
    whichCountry: (countries) => `কোন দেশ নিয়ে জানতে চান? যেসব দেশের গাইড আছে: ${countries}।`,
    testMode: "(পরীক্ষামূলক: এআই উত্তর এখনো চালু হয়নি।)",
    guideChosen: (guide) => `ঠিক আছে, *${guide}* গাইড। কী জানতে চান?`,
    noMatch: (guide) => `গাইড: *${guide}*। আপনার কথার সঙ্গে মেলে এমন অংশ পাইনি। অন্য শব্দে, বা ইংরেজি শব্দে চেষ্টা করুন।`,
    closest: (guide) => `*${guide}* গাইডের সবচেয়ে কাছের অংশ:`,
    sendText: "দয়া করে আপনার প্রশ্নটি লিখে পাঠান।",
    tooLong: `দয়া করে প্রশ্নটি ছোট করে পাঠান, ${bnDigits(MAX_CHARS)} অক্ষরের কম।`,
    personalRemoved:
      "আপনার নিরাপত্তার জন্য বার্তা থেকে এনআইডি, পাসপোর্ট, কার্ড বা ফোন নম্বরের মতো নম্বরটি সরিয়ে দিয়েছি। চ্যাটে এগুলো কখনো পাঠাবেন না।",
    error: "দুঃখিত, একটা সমস্যা হয়েছে। এক মিনিট পরে আবার চেষ্টা করুন।",
    refusal: {
      minute: "আপনি খুব দ্রুত বার্তা পাঠাচ্ছেন। এক মিনিট অপেক্ষা করে আবার জিজ্ঞেস করুন।",
      day: `আজকের প্রশ্নের সীমা শেষ। দয়া করে আগামীকাল আবার আসুন। ${HELP_LINE.bn}`,
      ip: `আজ আপনার নেটওয়ার্ক থেকে অনেক বেশি প্রশ্ন আসছে। দয়া করে আগামীকাল আবার চেষ্টা করুন। ${HELP_LINE.bn}`,
      sessions: `আপনার নেটওয়ার্ক থেকে অনেক নতুন চ্যাট খোলা হচ্ছে। এক ঘণ্টা পরে আবার চেষ্টা করুন। ${HELP_LINE.bn}`,
      budget: `নেভিগেটর আজ খুব ব্যস্ত। দয়া করে আগামীকাল আবার চেষ্টা করুন। ${HELP_LINE.bn}`,
      busy: `নেভিগেটর এখন খুব ব্যস্ত। এক মিনিট পরে আবার চেষ্টা করুন। ${HELP_LINE.bn}`,
    },
  },
};

/** For messages whose language we can't tell (a voice note, a photo): both languages. */
export function bilingual(pick: (m: Messages) => string): string {
  return `${pick(MESSAGES.bn)}\n${pick(MESSAGES.en)}`;
}
