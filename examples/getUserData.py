from sLIEa import SINoALICE
uuid = "YOUR UUID"
gameVer = '10.0.7'
client = SINoALICE(b"LOGIN ENCRYPT DATA", uuid, gameVer)
# client = SINoALICE("""LOGIN ENCRYPT DATA""", uuid)

print('-----------------------')
print('名稱: ', client.userData['name'])
print('個簽: ', client.userData['comment'])
print('戰力: ', client.userData['currentTotalPower'])
print('等級: ', client.userData['level'])
print('金幣: ', client.userData['money'])
print('魔晶石: ', client.userData['freeCurrentCoin'])
print('魔晶石(付費): ', client.userData['currentCoin'])
print('上次登入時間: ', client.userData['recentLoginTime'])
print('-----------------------')

input('點擊任意鍵...')
