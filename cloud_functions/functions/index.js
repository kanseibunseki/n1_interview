const functions = require('firebase-functions');
const OpenAI = require('openai');

// 環境に応じてconfigを取得する関数
const getConfig = () => {
  if (process.env.FUNCTIONS_EMULATOR) {
    // ローカルエミュレータ環境
    return require('./.runtimeconfig.json');
  } else {
    // プロダクション環境
    return functions.config();
  }
};

// configからOpenAI APIキーを取得
const config = getConfig();
const openaiApiKey = config.openai?.apikey;

if (!openaiApiKey) {
  console.error('OpenAI API key is not set');
  process.exit(1);
}

const openai = new OpenAI({
  apiKey: openaiApiKey,
});

exports.generateText = functions.https.onCall(async (data, context) => {
  // リクエストの検証
  if (!data.prompt || typeof data.prompt !== 'string') {
    throw new functions.https.HttpsError('invalid-argument', 'プロンプトは文字列で指定してください。');
  }

  try {
    const completion = await openai.completions.create({
      model: "text-davinci-003",
      prompt: data.prompt,
      max_tokens: 100
    });

    return { 
      success: true,
      result: completion.choices[0].text.trim(),
      usage: completion.usage
    };
  } catch (error) {
    console.error('OpenAI API error:', error);
    throw new functions.https.HttpsError('internal', 'OpenAI APIでエラーが発生しました。', error.message);
  }
});






// const functions = require('firebase-functions');
// const OpenAI = require('openai');

// const openaiApiKey = functions.config().openai?.apikey;
// if (!openaiApiKey) {
//   console.error('OpenAI API key is not set');
//   process.exit(1);
// }

// const openai = new OpenAI({
//   apiKey: openaiApiKey,
// });

// exports.generateText = functions.https.onCall(async (data, context) => {
//   // リクエストの検証
//   if (!data.prompt || typeof data.prompt !== 'string') {
//     throw new functions.https.HttpsError('invalid-argument', 'プロンプトは文字列で指定してください。');
//   }

//   try {
//     const completion = await openai.completions.create({
//       model: "text-davinci-003",
//       prompt: data.prompt,
//       max_tokens: 100
//     });

//     return { 
//       success: true,
//       result: completion.choices[0].text.trim(),
//       usage: completion.usage
//     };
//   } catch (error) {
//     console.error('OpenAI API error:', error);
//     throw new functions.https.HttpsError('internal', 'OpenAI APIでエラーが発生しました。', error.message);
//   }
// });