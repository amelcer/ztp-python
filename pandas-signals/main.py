import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import config


def fft_for_series(serie, length):
    fft = np.fft.fft(serie)
    freq = np.fft.fftfreq(length, d=1/config.fs)

    return [fft, freq]


df = pd.read_csv(config.csv_path)

duration = len(df) / config.fs
df.insert(0, 'czas', pd.Series([i / config.fs for i in range(len(df))]))
df.insert(len(df.columns), 'przyspieszenie', (df["ax"] **
          2 + df["ay"] ** 2 + df["az"] ** 2) ** 0.5)

df.to_csv(config.output_file, index=False)


df_length = len(df)
[fft_x, freq_x] = fft_for_series(df['ax'], df_length)
[fft_y, freq_y] = fft_for_series(df['ax'], df_length)
[fft_z, freq_z] = fft_for_series(df['az'], df_length)


# wykres FFT dla osi x
plt.plot(freq_x, np.abs(fft_x))
plt.title('FFT dla osi x')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.show()

# wykres FFT dla osi y
plt.plot(freq_y, np.abs(fft_y))
plt.title('FFT dla osi y')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.show()

# wykres FFT dla osi z
plt.plot(freq_z, np.abs(fft_z))
plt.title('FFT dla osi z')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.show()


max_freq_x = freq_x[np.abs(fft_x).argmax()]
max_freq_y = freq_y[np.abs(fft_y).argmax()]
max_freq_z = freq_z[np.abs(fft_z).argmax()]


df.insert(len(df.columns), 'fft_x', fft_x)
df.insert(len(df.columns), 'fft_y', fft_y)
df.insert(len(df.columns), 'fft_z', fft_z)
df.insert(len(df.columns), 'max_freq_x', max_freq_x)
df.insert(len(df.columns), 'max_freq_y', max_freq_y)
df.insert(len(df.columns), 'max_freq_z', fft_z)

df.to_csv(config.output_file + "-transformed", index=False)
