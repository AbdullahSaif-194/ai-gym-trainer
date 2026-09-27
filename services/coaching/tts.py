import asyncio
import threading
from io import BytesIO
import edge_tts


class TextToSpeech:
    # en-US-GuyNeural: energetic male coach voice, +20% speed feels natural for gym coaching
    VOICE = "en-US-GuyNeural"
    RATE  = "+20%"

    def speak(self, text, lang="en"):
        cleaned = (text or "").strip()

        if not cleaned:
            return None

        # Run in a separate thread with its own event loop —
        # asyncio.run() fails inside Streamlit because it already owns a loop
        result = [None]

        def run_in_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result[0] = loop.run_until_complete(self._generate(cleaned))
            except Exception as e:
                print(f"[TTS] Error generating audio: {e}")
            finally:
                loop.close()

        t = threading.Thread(target=run_in_thread)
        t.start()
        t.join()
        return result[0]

    async def _generate(self, text):
        tts = edge_tts.Communicate(text, voice=self.VOICE, rate=self.RATE)
        buf = BytesIO()

        async for chunk in tts.stream():
            if chunk["type"] == "audio":
                buf.write(chunk["data"])

        buf.seek(0)
        return buf.read()