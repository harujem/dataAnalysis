import win32com.client
speaker = win32com.client.Dispatch('SAPI.SpVoice')
speaker/Speak('안녕하세요? Hello. 12:21')
