import m3u8

original_m3u8_url = 'https://heritage-plus.evrideo.tv/05c9af40-9d2b-445b-ab20-5e46889877ce_1000010996_HLS/video_720p_1000010996.m3u8'
example_m3u8_master = 'https://bang-bang-tv-metaxsoft.evrideo.tv/fd7c895e-aa96-4298-ad6d-2be4936f5347_1000014572_HLS/master.m3u8'
example_m3u8_url = 'https://bang-bang-tv-metaxsoft.evrideo.tv/fd7c895e-aa96-4298-ad6d-2be4936f5347_1000014572_HLS/video_720p_1000014572.m3u8'

m3u8_obj = m3u8.load(example_m3u8_url)

print('\n'.join(m3u8_obj.dumps().splitlines()))
