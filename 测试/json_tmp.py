import json

s = r'{"code":"0000","innerCode":"0000","desc":"Success","message":{"servicevolume":18845922310201,"piearray":[{"totalvolume":11927501660442,"apptype":"4"},{"totalvolume":6185603556091,"apptype":"3"},{"totalvolume":6781422338100,"apptype":"99"},{"totalvolume":21024276349,"apptype":"1"},{"totalvolume":476753199,"apptype":"2"}],"sourcevolume":6070106273980,"linearray":[{"time":"20190221160000","servicevolume":82448895284,"sourcevolume":40997414735},{"time":"20190221160500","servicevolume":75538581127,"sourcevolume":43087288374},{"time":"20190221161000","servicevolume":71802772021,"sourcevolume":35857325169},{"time":"20190221161500","servicevolume":73643477875,"sourcevolume":36887089390},{"time":"20190221162000","servicevolume":75737454792,"sourcevolume":36404046563},{"time":"20190221162500","servicevolume":68892792635,"sourcevolume":38320889677},{"time":"20190221163000","servicevolume":73860047359,"sourcevolume":38981068926},{"time":"20190221163500","servicevolume":63390548750,"sourcevolume":27378952855},{"time":"20190221164000","servicevolume":64879383058,"sourcevolume":34674711422},{"time":"20190221164500","servicevolume":62330057776,"sourcevolume":32896278976},{"time":"20190221165000","servicevolume":56216358059,"sourcevolume":29620515311},{"time":"20190221165500","servicevolume":56716095584,"sourcevolume":27341622632},{"time":"20190221170000","servicevolume":57014122720,"sourcevolume":27736332177},{"time":"20190221170500","servicevolume":58813399506,"sourcevolume":27510477871},{"time":"20190221171000","servicevolume":58730875388,"sourcevolume":28879612421},{"time":"20190221171500","servicevolume":54439848492,"sourcevolume":28680436875},{"time":"20190221172000","servicevolume":54434158547,"sourcevolume":24573558101},{"time":"20190221172500","servicevolume":53751337466,"sourcevolume":21912362279},{"time":"20190221173000","servicevolume":47537749194,"sourcevolume":20574760446},{"time":"20190221173500","servicevolume":43751898725,"sourcevolume":22976728267},{"time":"20190221174000","servicevolume":44978565871,"sourcevolume":21454794901},{"time":"20190221174500","servicevolume":44827967915,"sourcevolume":23521180327},{"time":"20190221175000","servicevolume":41907280544,"sourcevolume":18445814085},{"time":"20190221175500","servicevolume":37814920938,"sourcevolume":18443452278},{"time":"20190221180000","servicevolume":34187279155,"sourcevolume":15311554138},{"time":"20190221180500","servicevolume":37278474239,"sourcevolume":18008052818},{"time":"20190221181000","servicevolume":39907969472,"sourcevolume":17651552269},{"time":"20190221181500","servicevolume":38976099445,"sourcevolume":15320717301},{"time":"20190221182000","servicevolume":38826864862,"sourcevolume":14465892633},{"time":"20190221182500","servicevolume":34585996865,"sourcevolume":14079985664},{"time":"20190221183000","servicevolume":31667532693,"sourcevolume":11842042957},{"time":"20190221183500","servicevolume":33596860266,"sourcevolume":13077766821},{"time":"20190221184000","servicevolume":35048623417,"sourcevolume":15214173644},{"time":"20190221184500","servicevolume":31315330583,"sourcevolume":11687072386},{"time":"20190221185000","servicevolume":29546490731,"sourcevolume":12657651584},{"time":"20190221185500","servicevolume":29737926109,"sourcevolume":13503238842},{"time":"20190221190000","servicevolume":30141698557,"sourcevolume":12641905412},{"time":"20190221190500","servicevolume":30104956462,"sourcevolume":15737060830},{"time":"20190221191000","servicevolume":31969338730,"sourcevolume":14893496376},{"time":"20190221191500","servicevolume":29740146082,"sourcevolume":13650624208},{"time":"20190221192000","servicevolume":28700088943,"sourcevolume":14276050242},{"time":"20190221192500","servicevolume":28075824721,"sourcevolume":9312205670},{"time":"20190221193000","servicevolume":31530433620,"sourcevolume":14756104813},{"time":"20190221193500","servicevolume":27559913796,"sourcevolume":9394706386},{"time":"20190221194000","servicevolume":25230430235,"sourcevolume":10807777114},{"time":"20190221194500","servicevolume":25082573619,"sourcevolume":7332222143},{"time":"20190221195000","servicevolume":29015478391,"sourcevolume":8858480103},{"time":"20190221195500","servicevolume":26700129903,"sourcevolume":8465946908},{"time":"20190221200000","servicevolume":24213247785,"sourcevolume":8155217083},{"time":"20190221200500","servicevolume":23298833765,"sourcevolume":9069939118},{"time":"20190221201000","servicevolume":24382009730,"sourcevolume":8245850295},{"time":"20190221201500","servicevolume":25044985999,"sourcevolume":5859145112},{"time":"20190221202000","servicevolume":20335689895,"sourcevolume":8039543947},{"time":"20190221202500","servicevolume":20998993655,"sourcevolume":7376255702},{"time":"20190221203000","servicevolume":23603179903,"sourcevolume":6068506231},{"time":"20190221203500","servicevolume":21772280850,"sourcevolume":6761331763},{"time":"20190221204000","servicevolume":19274441585,"sourcevolume":6761577861},{"time":"20190221204500","servicevolume":18894583465,"sourcevolume":7330806033},{"time":"20190221205000","servicevolume":22329936775,"sourcevolume":6331731164},{"time":"20190221205500","servicevolume":19061955018,"sourcevolume":6754673920},{"time":"20190221210000","servicevolume":16978427822,"sourcevolume":7676068581},{"time":"20190221210500","servicevolume":20535557493,"sourcevolume":6195723869},{"time":"20190221211000","servicevolume":22518483173,"sourcevolume":6400492496},{"time":"20190221211500","servicevolume":22733174651,"sourcevolume":7283771433},{"time":"20190221212000","servicevolume":22430993002,"sourcevolume":8440921007},{"time":"20190221212500","servicevolume":25450933539,"sourcevolume":8349340363},{"time":"20190221213000","servicevolume":27551381562,"sourcevolume":6105574540},{"time":"20190221213500","servicevolume":23896562929,"sourcevolume":7065365450},{"time":"20190221214000","servicevolume":23002579206,"sourcevolume":7945352319},{"time":"20190221214500","servicevolume":23908632972,"sourcevolume":7345776128},{"time":"20190221215000","servicevolume":26072010104,"sourcevolume":5517639990},{"time":"20190221215500","servicevolume":27980255172,"sourcevolume":5962698264},{"time":"20190221220000","servicevolume":25203840030,"sourcevolume":5594600159},{"time":"20190221220500","servicevolume":24825861990,"sourcevolume":7953361979},{"time":"20190221221000","servicevolume":26334464149,"sourcevolume":7956027042},{"time":"20190221221500","servicevolume":28322438173,"sourcevolume":7658215118},{"time":"20190221222000","servicevolume":35445689830,"sourcevolume":10788141288},{"time":"20190221222500","servicevolume":28823139077,"sourcevolume":9893105321},{"time":"20190221223000","servicevolume":31190794191,"sourcevolume":8581409510},{"time":"20190221223500","servicevolume":36365418894,"sourcevolume":10254786900},{"time":"20190221224000","servicevolume":35487783089,"sourcevolume":8793540390},{"time":"20190221224500","servicevolume":41175160293,"sourcevolume":10679514257},{"time":"20190221225000","servicevolume":36454461377,"sourcevolume":10333077109},{"time":"20190221225500","servicevolume":48563324924,"sourcevolume":12825218643},{"time":"20190221230000","servicevolume":56904906578,"sourcevolume":13563086041},{"time":"20190221230500","servicevolume":47786492529,"sourcevolume":15955111841},{"time":"20190221231000","servicevolume":49092717084,"sourcevolume":15133921539},{"time":"20190221231500","servicevolume":52994239312,"sourcevolume":14813700355},{"time":"20190221232000","servicevolume":57749813929,"sourcevolume":16030030878},{"time":"20190221232500","servicevolume":59945406193,"sourcevolume":15076630803},{"time":"20190221233000","servicevolume":55157813982,"sourcevolume":15231796803},{"time":"20190221233500","servicevolume":68744892218,"sourcevolume":13971825026},{"time":"20190221234000","servicevolume":74324884097,"sourcevolume":22602676302},{"time":"20190221234500","servicevolume":69891778498,"sourcevolume":16970039142},{"time":"20190221235000","servicevolume":68080886682,"sourcevolume":16755935877},{"time":"20190221235500","servicevolume":77396885395,"sourcevolume":19477171137},{"time":"20190222000000","servicevolume":82492008230,"sourcevolume":21100310594},{"time":"20190222000500","servicevolume":85027383898,"sourcevolume":23611444093},{"time":"20190222001000","servicevolume":89641684195,"sourcevolume":20357196727},{"time":"20190222001500","servicevolume":93893109062,"sourcevolume":21009088002},{"time":"20190222002000","servicevolume":91631497413,"sourcevolume":22476489082},{"time":"20190222002500","servicevolume":91627839256,"sourcevolume":22044889507},{"time":"20190222003000","servicevolume":96781684610,"sourcevolume":21765905417},{"time":"20190222003500","servicevolume":107951098449,"sourcevolume":26170180519},{"time":"20190222004000","servicevolume":118615464153,"sourcevolume":22353965853},{"time":"20190222004500","servicevolume":112832056031,"sourcevolume":23525898249},{"time":"20190222005000","servicevolume":113907780081,"sourcevolume":21096061719},{"time":"20190222005500","servicevolume":121378338104,"sourcevolume":27943214652},{"time":"20190222010000","servicevolume":125066662823,"sourcevolume":25426489540},{"time":"20190222010500","servicevolume":135597736468,"sourcevolume":26208119803},{"time":"20190222011000","servicevolume":141283468717,"sourcevolume":28887656496},{"time":"20190222011500","servicevolume":139059414824,"sourcevolume":26188856199},{"time":"20190222012000","servicevolume":139986282771,"sourcevolume":29098702295},{"time":"20190222012500","servicevolume":150946434793,"sourcevolume":35322733912},{"time":"20190222013000","servicevolume":141449047674,"sourcevolume":30823586229},{"time":"20190222013500","servicevolume":137469862021,"sourcevolume":28430128279},{"time":"20190222014000","servicevolume":146764397240,"sourcevolume":28163617287},{"time":"20190222014500","servicevolume":124109671300,"sourcevolume":27421489375},{"time":"20190222015000","servicevolume":134898785961,"sourcevolume":29748732872},{"time":"20190222015500","servicevolume":138312873848,"sourcevolume":32608992191},{"time":"20190222020000","servicevolume":117180622766,"sourcevolume":26481912895},{"time":"20190222020500","servicevolume":113264056264,"sourcevolume":24725043818},{"time":"20190222021000","servicevolume":129597864662,"sourcevolume":33477868499},{"time":"20190222021500","servicevolume":111218630166,"sourcevolume":32620904208},{"time":"20190222022000","servicevolume":118394096809,"sourcevolume":31060774979},{"time":"20190222022500","servicevolume":111754622577,"sourcevolume":34067597367},{"time":"20190222023000","servicevolume":117204025082,"sourcevolume":39059605582},{"time":"20190222023500","servicevolume":119337627807,"sourcevolume":36096056944},{"time":"20190222024000","servicevolume":124550059925,"sourcevolume":31766576959},{"time":"20190222024500","servicevolume":121108085352,"sourcevolume":33426622723},{"time":"20190222025000","servicevolume":120451928122,"sourcevolume":28766129564},{"time":"20190222025500","servicevolume":110810300698,"sourcevolume":30616630316},{"time":"20190222030000","servicevolume":121702979223,"sourcevolume":32317682197},{"time":"20190222030500","servicevolume":110977555412,"sourcevolume":37948370133},{"time":"20190222031000","servicevolume":105993354408,"sourcevolume":30627912203},{"time":"20190222031500","servicevolume":105254249074,"sourcevolume":32132945866},{"time":"20190222032000","servicevolume":121007877391,"sourcevolume":33672587058},{"time":"20190222032500","servicevolume":109999306025,"sourcevolume":43536254386},{"time":"20190222033000","servicevolume":120177808628,"sourcevolume":31549258012},{"time":"20190222033500","servicevolume":106111705289,"sourcevolume":33510026299},{"time":"20190222034000","servicevolume":105408881239,"sourcevolume":33008501111},{"time":"20190222034500","servicevolume":98678260233,"sourcevolume":30969432435},{"time":"20190222035000","servicevolume":106446448757,"sourcevolume":33649359622},{"time":"20190222035500","servicevolume":106394037410,"sourcevolume":36881590355},{"time":"20190222040000","servicevolume":98526194030,"sourcevolume":34754065098},{"time":"20190222040500","servicevolume":100282884678,"sourcevolume":38412307543},{"time":"20190222041000","servicevolume":101356609256,"sourcevolume":32967345137},{"time":"20190222041500","servicevolume":101352581545,"sourcevolume":33541615179},{"time":"20190222042000","servicevolume":107753587931,"sourcevolume":37522173866},{"time":"20190222042500","servicevolume":103360776786,"sourcevolume":38161484042},{"time":"20190222043000","servicevolume":114141639139,"sourcevolume":35417409282},{"time":"20190222043500","servicevolume":113325989015,"sourcevolume":40513539200},{"time":"20190222044000","servicevolume":112753923339,"sourcevolume":32369058503},{"time":"20190222044500","servicevolume":105531622798,"sourcevolume":39490263535},{"time":"20190222045000","servicevolume":121689487718,"sourcevolume":39565743470},{"time":"20190222045500","servicevolume":117346894310,"sourcevolume":36794385832},{"time":"20190222050000","servicevolume":104499116123,"sourcevolume":33525691884},{"time":"20190222050500","servicevolume":105258741319,"sourcevolume":36156479982},{"time":"20190222051000","servicevolume":104986076503,"sourcevolume":31021616991},{"time":"20190222051500","servicevolume":105355895133,"sourcevolume":34853050899},{"time":"20190222052000","servicevolume":114302607306,"sourcevolume":35146179181},{"time":"20190222052500","servicevolume":116512631122,"sourcevolume":34412627373},{"time":"20190222053000","servicevolume":115685236142,"sourcevolume":34549270317},{"time":"20190222053500","servicevolume":104309265220,"sourcevolume":35810577627},{"time":"20190222054000","servicevolume":119499159128,"sourcevolume":33429519316},{"time":"20190222054500","servicevolume":116114818311,"sourcevolume":38832422854},{"time":"20190222055000","servicevolume":101293292370,"sourcevolume":31486930677},{"time":"20190222055500","servicevolume":98399263229,"sourcevolume":30244630313},{"time":"20190222060000","servicevolume":114517758273,"sourcevolume":38282650106},{"time":"20190222060500","servicevolume":102889422622,"sourcevolume":33389715857},{"time":"20190222061000","servicevolume":107305555931,"sourcevolume":38258526914},{"time":"20190222061500","servicevolume":105442583936,"sourcevolume":32062998476},{"time":"20190222062000","servicevolume":102638932849,"sourcevolume":30502119339},{"time":"20190222062500","servicevolume":102754113204,"sourcevolume":31581101039},{"time":"20190222063000","servicevolume":116867275244,"sourcevolume":32815431745},{"time":"20190222063500","servicevolume":119202040421,"sourcevolume":36514757813},{"time":"20190222064000","servicevolume":125855595290,"sourcevolume":33735948853},{"time":"20190222064500","servicevolume":116262508219,"sourcevolume":36869797035},{"time":"20190222065000","servicevolume":115406954429,"sourcevolume":34557009980},{"time":"20190222065500","servicevolume":111660602137,"sourcevolume":41445725862},{"time":"20190222070000","servicevolume":114215470684,"sourcevolume":38093592166},{"time":"20190222070500","servicevolume":122016163960,"sourcevolume":35358901023},{"time":"20190222071000","servicevolume":125258617899,"sourcevolume":38475609365},{"time":"20190222071500","servicevolume":131150433238,"sourcevolume":43467327819},{"time":"20190222072000","servicevolume":119957756399,"sourcevolume":38508224907},{"time":"20190222072500","servicevolume":113891737079,"sourcevolume":43108310251},{"time":"20190222073000","servicevolume":114972790405,"sourcevolume":36102833354},{"time":"20190222073500","servicevolume":122673199519,"sourcevolume":36483230552},{"time":"20190222074000","servicevolume":130674235854,"sourcevolume":37970286721},{"time":"20190222074500","servicevolume":128284436237,"sourcevolume":38319702540},{"time":"20190222075000","servicevolume":126684638751,"sourcevolume":38782462330},{"time":"20190222075500","servicevolume":125183524773,"sourcevolume":45159267873},{"time":"20190222080000","servicevolume":117633294887,"sourcevolume":38888945423},{"time":"20190222080500","servicevolume":134679619159,"sourcevolume":42492608851},{"time":"20190222081000","servicevolume":128986584507,"sourcevolume":42613790519},{"time":"20190222081500","servicevolume":125716887128,"sourcevolume":38326154182},{"time":"20190222082000","servicevolume":127918585810,"sourcevolume":35461469223},{"time":"20190222082500","servicevolume":116665445202,"sourcevolume":38437387728},{"time":"20190222083000","servicevolume":113276711684,"sourcevolume":37153254992},{"time":"20190222083500","servicevolume":121867601385,"sourcevolume":46953635121},{"time":"20190222084000","servicevolume":118073777809,"sourcevolume":41543811815},{"time":"20190222084500","servicevolume":127803294525,"sourcevolume":41955444935},{"time":"20190222085000","servicevolume":123784835703,"sourcevolume":46392425816},{"time":"20190222085500","servicevolume":121319747633,"sourcevolume":42417718618},{"time":"20190222090000","servicevolume":115987228788,"sourcevolume":42152945242},{"time":"20190222090500","servicevolume":123431596468,"sourcevolume":43634529575},{"time":"20190222091000","servicevolume":120023837455,"sourcevolume":40103321992},{"time":"20190222091500","servicevolume":127922039171,"sourcevolume":46495369400},{"time":"20190222092000","servicevolume":122662469879,"sourcevolume":45382872288},{"time":"20190222092500","servicevolume":114815593048,"sourcevolume":42730459405},{"time":"20190222093000","servicevolume":124705152019,"sourcevolume":46814487069},{"time":"20190222093500","servicevolume":112326552845,"sourcevolume":41695787830},{"time":"20190222094000","servicevolume":112404730708,"sourcevolume":44142879417},{"time":"20190222094500","servicevolume":120026484156,"sourcevolume":45979594537},{"time":"20190222095000","servicevolume":111343796633,"sourcevolume":42369139828},{"time":"20190222095500","servicevolume":120312014242,"sourcevolume":45772777708},{"time":"20190222100000","servicevolume":128640715374,"sourcevolume":45781906781},{"time":"20190222100500","servicevolume":115667499149,"sourcevolume":49965284396},{"time":"20190222101000","servicevolume":119935797117,"sourcevolume":43159697689},{"time":"20190222101500","servicevolume":120823093228,"sourcevolume":47928706463},{"time":"20190222102000","servicevolume":118610730974,"sourcevolume":39619921648},{"time":"20190222102500","servicevolume":121035763357,"sourcevolume":43618198375},{"time":"20190222103000","servicevolume":115785239606,"sourcevolume":47782577150},{"time":"20190222103500","servicevolume":110507238462,"sourcevolume":40431159651},{"time":"20190222104000","servicevolume":113557473959,"sourcevolume":41291476420}]},"summarymessage":null,"success":true}'
s = r'{"count":3458840096,"_shards":{"total":210,"successful":210,"skipped":0,"failed":0}}'
tmp_dict = json.loads(s)
print(tmp_dict['count'])

exit()

# print(tmp_dict['message']['linearray'])
service_rate = list()
for item in tmp_dict['message']['linearray']:
    # print(item['servicevolume'])
    service_rate.append(item['servicevolume'])

print(max(service_rate)/1024/1024/1024)





