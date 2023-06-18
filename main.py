# Remember to use your own values from my.telegram.org!
api_id = 1234
api_hash = '12345'

from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.types import InputChannel, InputPeerChannel

with TelegramClient('anon', api_id, api_hash) as client:
    result = client(functions.channels.CreateChannelRequest(
        title='SW systems 2 task',
        about='SW systems 2 task',
        megagroup=False
    ))
    desiredPublicUsername = "PodanenkoDenysSW2TaskChannel"
    channelId = result.chats[0].id
    channelAccessHash = result.chats[0].access_hash
    checkUsernameResult = client(CheckUsernameRequest(InputPeerChannel(channel_id=channelId, access_hash=channelAccessHash), desiredPublicUsername))
    #print(checkUsernameResult)
    if(checkUsernameResult==True):
        publicChannel = client(UpdateUsernameRequest(InputPeerChannel(channel_id=channelId, access_hash=channelAccessHash), desiredPublicUsername))
        #print(publicChannel)
    print(result.stringify())
    
    channel = client.get_entity(channelId)

    client.send_message(channel, 'E-commerce (electronic commerce) is the activity of electronically buying or selling of products on online services or over the Internet. E-commerce draws on technologies such as mobile commerce, electronic funds transfer, supply chain management, Internet marketing, online transaction processing, electronic data interchange (EDI), inventory management systems, and automated data collection systems. E-commerce is in turn driven by the technological advances of the semiconductor industry, and is the largest sector of the electronics industry.')
    client.send_message(channel, 'Contemporary electronic commerce can be classified into two categories. The first category is business based on types of goods sold (involves everything from ordering "digital" content for immediate online consumption, to ordering conventional goods and services, to "meta" services to facilitate other types of electronic commerce). The second category is based on the nature of the participant (B2B, B2C, C2B and C2C).[7]On the institutional level, big corporations and financial institutions use the internet to exchange financial data to facilitate domestic and international business. Data integrity and security are pressing issues for electronic commerce.Aside from traditional e-commerce, the terms m-Commerce (mobile commerce) as well (around 2013) t-Commerce[8] have also been used.')    
    client.send_message(channel, 'In the United States, Californias Electronic Commerce Act (1984), enacted by the Legislature, the more recent California Privacy Rights Act (2020), enacted through a popular election proposition and to control specifically how electronic commerce may be conducted in California. In the US in its entirety, electronic commerce activities are regulated more broadly by the Federal Trade Commission (FTC). These activities include the use of commercial e-mails, online advertising and consumer privacy. The CAN-SPAM Act of 2003 establishes national standards for direct marketing over e-mail. The Federal Trade Commission Act regulates all forms of advertising, including online advertising, and states that advertising must be truthful and non-deceptive.[9] Using its authority under Section 5 of the FTC Act, which prohibits unfair or deceptive practices, the FTC has brought a number of cases to enforce the promises in corporate privacy statements, including promises about the security of consumers personal information.[10] As a result, any corporate privacy policy related to e-commerce activity may be subject to enforcement by the FTC.')
    client.send_message(channel, 'Internationally there is the International Consumer Protection and Enforcement Network (ICPEN), which was formed in 1991 from an informal network of government customer fair trade organisations. The purpose was stated as being to find ways of co-operating on tackling consumer problems connected with cross-border transactions in both goods and services, and to help ensure exchanges of information among the participants for mutual benefit and understanding. From this came Econsumer.gov, an ICPEN initiative since April 2001. It is a portal to report complaints about online and related transactions with foreign companies.')
    client.send_message(channel, 'In 2010, the United Kingdom had the highest per capita e-commerce spending in the world.[23] As of 2013, the Czech Republic was the European country where e-commerce delivers the biggest contribution to the enterprises total revenue. Almost a quarter (24%) of the countrys total turnover is generated via the online channel.[24]')
    client.send_message(channel, 'Among emerging economies, Chinas e-commerce presence continues to expand every year. With 668 million Internet users, Chinas online shopping sales reached $253 billion in the first half of 2015, accounting for 10% of total Chinese consumer retail sales in that period.[25] The Chinese retailers have been able to help consumers feel more comfortable shopping online.[26] e-commerce transactions between China and other countries increased 32% to 2.3 trillion yuan ($375.8 billion) in 2012 and accounted for 9.6% of Chinas total international trade.[27] In 2013, Alibaba had an e-commerce market share of 80% in China.[28] In 2014, Alibaba still dominated the B2B marketplace in China with a market share of 44.82%, followed by several other companies including Made-in-China.com at 3.21%, and GlobalSources.com at 2.98%, with the total transaction value of Chinas B2B market exceeding 4.5 billion yuan.[29]In 2014, there were 600 million Internet users in China (twice as many as in the US), making it the worlds biggest online market.[30] China is also the largest e-commerce market in the world by value of sales, with an estimated US$899 billion in 2016.[31] Research shows that Chinese consumer motivations are different enough from Western audiences to require unique e-commerce app designs instead of simply porting Western apps into the Chinese market.[32]')
    client.send_message(channel, 'Recent research indicates that electronic commerce, commonly referred to as e-commerce, presently shapes the manner in which people shop for products. The GCC countries have a rapidly growing market and are characterized by a population that becomes wealthier (Yuldashev). As such, retailers have launched Arabic-language websites as a means to target this population. Secondly, there are predictions of increased mobile purchases and an expanding internet audience (Yuldashev). The growth and development of the two aspects make the GCC countries become larger players in the electronic commerce market with time progress. Specifically, research shows that the e-commerce market is expected to grow to over $20 billion by 2020 among these GCC countries (Yuldashev). The e-commerce market has also gained much popularity among western countries, and in particular Europe and the U.S. These countries have been highly characterized by consumer-packaged goods (CPG) (Geisler, 34). However, trends show that there are future signs of a reverse. Similar to the GCC countries, there has been increased purchase of goods and services in online channels rather than offline channels. Activist investors are trying hard to consolidate and slash their overall cost and the governments in western countries continue to impose more regulation on CPG manufacturers (Geisler, 36). In these senses, CPG investors are being forced to adapt to e-commerce as it is effective as well as a means for them to thrive.')
    client.send_message(channel, 'In 2013, Brazils e-commerce was growing quickly with retail e-commerce sales expected to grow at a double-digit pace through 2014. By 2016, eMarketer expected retail e-commerce sales in Brazil to reach $17.3 billion.[33] India has an Internet user base of about 460 million as of December 2017.[34] Despite being the third largest user base in the world, the penetration of the Internet is low compared to markets like the United States, United Kingdom or France but is growing at a much faster rate, adding around 6 million new entrants every month.[citation needed] In India, cash on delivery is the most preferred payment method, accumulating 75% of the e-retail activities.[35][citation needed] The India retail market is expected to rise from 2.5% in 2016 to 5% in 2020.[36]')
    client.send_message(channel, 'The future trends in the GCC countries will be similar to that of the western countries. Despite the forces that push business to adapt e-commerce as a means to sell goods and products, the manner in which customers make purchases is similar in countries from these two regions. For instance, there has been an increased usage of smartphones which comes in conjunction with an increase in the overall internet audience from the regions. Yuldashev writes that consumers are scaling up to more modern technology that allows for mobile marketing. However, the percentage of smartphone and internet users who make online purchases is expected to vary in the first few years. It will be independent on the willingness of the people to adopt this new trend (The Statistics Portal). For example, UAE has the greatest smartphone penetration of 73.8 per cent and has 91.9 per cent of its population has access to the internet. On the other hand, smartphone penetration in Europe has been reported to be at 64.7 per cent (The Statistics Portal). Regardless, the disparity in percentage between these regions is expected to level out in future because e-commerce technology is expected to grow to allow for more users.')
    client.send_message(channel, 'The e-commerce business within these two regions will result in competition. Government bodies at the country level will enhance their measures and strategies to ensure sustainability and consumer protection (Krings, et al.). These increased measures will raise the environmental and social standards in the countries, factors that will determine the success of the e-commerce market in these countries. For example, an adoption of tough sanctions will make it difficult for companies to enter the e-commerce market while lenient sanctions will allow ease of companies. As such, the future trends between GCC countries and the Western countries will be independent of these sanctions (Krings, et al.). These countries need to make rational conclusions in coming up with effective sanctions.')

    print(f'Info About channel:\n ID:{channel.id}\n Username:{channel.username}\n Title:{channel.title}\n CreationDate:{channel.date}')

    posts = client(functions.messages.GetHistoryRequest(
        peer=channel,
        limit=8000,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

    #print(posts)

    for i in range(5):
        print(f'--Message {i+1}--\nDate:{posts.messages[i].date}\nContent:{posts.messages[i].message}\nNumber of characters:{len(posts.messages[i].message)}\nNumber of words:{len(posts.messages[i].message.split())}')