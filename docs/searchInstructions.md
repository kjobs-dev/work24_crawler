1. search jobs page link: https://www.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do

2. Search section HTML:
<div class="renewal_EmpSrch">
	<article class="box_border_type fill mt24" id="obj_set">
		<div class="search_more_type type_fit">
			<ul>
				<li>
					<div class="tit b1_sb">
						검색어 범위
					</div>
					<div class="cont">
						<div class="box_chk-group">
							
							
								
							
							<span>
								<input type="checkbox" onclick="f_keywordTextCheck('srcKeyword','');" id="srckeywordAllChk" name="keywordStaAreaNm_" value="Y" checked="checked">
								<label for="srckeywordAllChk">전체</label>
							</span>
							<span>
								<input type="checkbox" onclick="f_keywordTextCheck('srcKeyword','keywordWantedTitle');" id="srckeywordWantedTitle" name="srckeywordWantedTitle" value="Y">
							<label for="srckeywordWantedTitle">제목</label>
							</span>
							<span>
								<input type="checkbox" onclick="f_keywordTextCheck('srcKeyword','keywordBusiNm');" id="srckeywordBusiNm" name="srckeywordBusiNm" value="Y">
								<label for="srckeywordBusiNm">회사명</label>
							</span>
							<span>
								<input type="checkbox" onclick="f_keywordTextCheck('srcKeyword','keywordJobCont');" id="srckeywordJobCont" name="srckeywordJobCont" value="Y">
								<label for="srckeywordJobCont">직무내용</label>
							</span>
							<span>
								<input type="checkbox" onclick="f_keywordTextCheck('srcKeyword','keywordStaAreaNm');" id="srckeywordStaAreaNm" name="srckeywordStaAreaNm" value="Y">
								<label for="srckeywordStaAreaNm">역세권명</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<div class="tit b1_sb">
						검색어
						<div class="box_tooltip bottom">
							<button type="button" class="btn_help dis"><span class="blind">도움말</span></button>
							<div class="box_help-data w_big">
								<p class="s1_sb">검색어 검색 안내</p>
								<p class="txt_list">검색어 검색 시 검색연산자를 활용하면 원하는 결과를 쉽고 빠르게 검색할 수 있습니다. (검색연산자는 중복 사용 가능합니다.)</p>
								<div class="box_table_wrap">
									<!-- table -->
									<table class="box_table mt16"><caption>연산자,예시,검색내용을(를) 제공하는 표</caption>

										<colgroup>
											<col style="width:20%">
											<col style="width:25%">
											<col>
										</colgroup>
										<thead>
										<tr>
											<th scope="col">연산자</th>
											<th scope="col">예시</th>
											<th scope="col">검색내용</th>

										</tr>
										</thead>
										<tbody>
										<tr>
											<td scope="row">띄어쓰기</td>
											<td>영업 해외영업</td>
											<td>[영업]과 [해외영업] 모두 포함된 결과값을 검색(AND)</td>
										</tr>
										<tr>
											<td scope="row">
												<span class="b1_r">|</span>
												<button onclick="fn_textCopyOnClipBoard('|')" type="button" class="btn xsmall type02"><span>문자복사</span></button>
											</td>
											<td>영업 | 해외영업</td>
											<td>[영업]과 [해외영업] 중 하나 이상 포함된 결과값을 검색(OR)</td>
										</tr>
										</tbody>
									</table>
								</div>
								<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span></button>
							</div>
						</div>
					</div>
					<div class="cont">
						<div class="box_table_group">
							<div class="cell"> <!-- D: error 일경우 class[error] add -->
								<span class="box_ipt">
									<input type="text" id="srcKeyword" class="input_txt medium" title="검색어를 입력해 주세요." value="" maxlength="30" onfocus="input_limit_string(this,'/kor,/eng,/d,/symbol7,/s');" placeholder="여러단어를 입력하실 때는 띄어쓰기(AND), |(OR) 연산자를 이용하여 더욱 세밀하게 검색 가능합니다.">
									<button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
								</span>
							</div>
						</div>
						
					</div>
				</li>
				<li>
					<div class="tit b1_sb">
						제외 검색어
						<div class="box_tooltip">
							<button type="button" class="btn_help dis"><span class="blind">도움말</span></button>
							<div class="box_help-data w_big">
								<p class="s1_sb">제외 검색어</p>
								<p class="txt_list">입력란에 제외할 단어를 입력하세요. 여러 단어를 제외하고 싶은 경우 쉼표(,)를 사용하여 작성 가능합니다.</p>
								<div class="box_table_wrap mt16">
									<!-- table -->
									<table class="box_table"><caption>연산자,예시,검색내용을(를) 제공하는 표</caption>

										<colgroup>
											<col style="width:20%">
											<col style="width:30%">
											<col>
										</colgroup>
										<thead>
										<tr>
											<th scope="col">연산자</th>
											<th scope="col">예시</th>
											<th scope="col">검색내용</th>
										</tr>
										</thead>
										<tbody>
										<tr>
											<td scope="row">,</td>
											<td>제가요양보호사, 돌봄서비스</td>
											<td>입력한 검색어를 제외하고 검색 (NOT)</td>
										</tr>
										</tbody>
									</table>
								</div>
								<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span></button>
							</div>
						</div>
					</div>
					<div class="cont">
						<div class="box_table_group">
							<div class="cell"> <!-- D: error 일경우 class[error] add -->
								<span class="box_ipt">
									<input type="text" id="notSrcKeyword" class="input_txt medium" title="제외 검색어를 입력해 주세요." value="" maxlength="30" onfocus="input_limit_string(this,'/kor,/eng,/d,/symbol8,/s');" onkeypress="if(event.keyCode==13) goSubmit();" placeholder="검색결과에서 제외할 단어를 입력하세요. 여러 단어는 쉼표(,)로 작성이 가능합니다.">
									<button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
								</span>
							</div>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">직종</span>
					<div class="cont">
						<!-- <button type="button" class="btn medium type02 full_open" open-full-pop="full_wk-jobs-search" id="jopFinder"><span>직종 선택</span></button> -->
						<button type="button" class="btn medium mw_auto type02" onclick="fn_show('jobCategory');"><span>직종선택</span></button>
						<div id="jobCategory" style="" class="layer_section on">

							<!-- 본문 컨텐츠 -->
							<!-- 250416 article 태그 삭제 -->
							<ul class="box_list_area">
								<li class="txt_list">직종 : 최대 10개의 직종 선택이 가능합니다. 원하시는 직종을 선택하세요.</li>
								<li class="txt_list">체크박스를 클릭하면 직종이 선택되고, ‘직종명’을 클릭하면 하위 분류가 보여집니다.</li>
								<li class="txt_list">3차 분류 직종을 선택하시면 해당 직종에 대한 키워드로 채용정보를 검색하실 수 있습니다.</li>
							</ul>
							<table class="search_table mt16"><caption>검색키워드을(를) 제공하는 표</caption>
								
								<colgroup>
									<col style="width:16%;">
									<col>
								</colgroup>
								<tbody>
								<tr>
									<th scope="row"><span>검색키워드</span></th>
									<td>
										<div class="box_sch_group">
												<span class="box_ipt">
													<input type="text" id="jobSearchKeyword" name="" class="input_txt" title="직종 키워드를 입력해 주세요. 예) 영업,운전, 사무" value="" placeholder="직종 키워드를 입력해 주세요. 예) 영업,운전, 사무">
													<button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
												</span>
											<button type="button" class="btn medium fill type01" onclick="jobCategorySearch();">검색</button>
										</div>
									</td>
								</tr>
								</tbody>
							</table>

							<div id="wk-jobs-search-view1">
								<div class="list_chk_area type_col chk_col_type mt16">
									<div class="col">
										<p class="tit">1차 분류</p>
										<div class="cont_area scroll h280">
											<ul class="box_chk-group chk_row" id="mainJobDiv"><li><span class="pt08"><input type="checkbox" id="chk08" name="mainJob" title="건설·채굴 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'08');" value="08"><label for="chk08"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName08" title="건설·채굴에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('08', 'mainJob0' , 'subJob');">건설·채굴</button><input type="hidden" id="mainJob0Nm" value="건설·채굴"><input type="hidden" name="firstJobName" id="jobName08" value="건설·채굴"></li><li><span class="pt08"><input type="checkbox" id="chk01" name="mainJob" title="경영·사무·금융·보험 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'01');" value="01"><label for="chk01"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName01" title="경영·사무·금융·보험에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('01', 'mainJob1' , 'subJob');">경영·사무·금융·보험</button><input type="hidden" id="mainJob1Nm" value="경영·사무·금융·보험"><input type="hidden" name="firstJobName" id="jobName01" value="경영·사무·금융·보험"></li><li><span class="pt08"><input type="checkbox" id="chk03" name="mainJob" title="교육·법률·사회복지·경찰·소방 및 군인 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'03');" value="03"><label for="chk03"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName03" title="교육·법률·사회복지·경찰·소방 및 군인에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('03', 'mainJob2' , 'subJob');">교육·법률·사회복지·경찰·소방 및 군인</button><input type="hidden" id="mainJob2Nm" value="교육·법률·사회복지·경찰·소방 및 군인"><input type="hidden" name="firstJobName" id="jobName03" value="교육·법률·사회복지·경찰·소방 및 군인"></li><li><span class="pt08"><input type="checkbox" id="chk13" name="mainJob" title="농림어업직 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'13');" value="13"><label for="chk13"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName13" title="농림어업직에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('13', 'mainJob3' , 'subJob');">농림어업직</button><input type="hidden" id="mainJob3Nm" value="농림어업직"><input type="hidden" name="firstJobName" id="jobName13" value="농림어업직"></li><li><span class="pt08"><input type="checkbox" id="chk06" name="mainJob" title="미용·여행·숙박·음식·경비·돌봄·청소 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'06');" value="06"><label for="chk06"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName06" title="미용·여행·숙박·음식·경비·돌봄·청소에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('06', 'mainJob4' , 'subJob');">미용·여행·숙박·음식·경비·돌봄·청소</button><input type="hidden" id="mainJob4Nm" value="미용·여행·숙박·음식·경비·돌봄·청소"><input type="hidden" name="firstJobName" id="jobName06" value="미용·여행·숙박·음식·경비·돌봄·청소"></li><li><span class="pt08"><input type="checkbox" id="chk04" name="mainJob" title="보건·의료 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'04');" value="04"><label for="chk04"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName04" title="보건·의료에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('04', 'mainJob5' , 'subJob');">보건·의료</button><input type="hidden" id="mainJob5Nm" value="보건·의료"><input type="hidden" name="firstJobName" id="jobName04" value="보건·의료"></li><li><span class="pt08"><input type="checkbox" id="chk09" name="mainJob" title="설치·정비·생산-기계·금속·재료 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'09');" value="09"><label for="chk09"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName09" title="설치·정비·생산-기계·금속·재료에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('09', 'mainJob6' , 'subJob');">설치·정비·생산-기계·금속·재료</button><input type="hidden" id="mainJob6Nm" value="설치·정비·생산-기계·금속·재료"><input type="hidden" name="firstJobName" id="jobName09" value="설치·정비·생산-기계·금속·재료"></li><li><span class="pt08"><input type="checkbox" id="chk12" name="mainJob" title="설치·정비·생산-인쇄·목재·공예 및 제조 단순 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'12');" value="12"><label for="chk12"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName12" title="설치·정비·생산-인쇄·목재·공예 및 제조 단순에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('12', 'mainJob7' , 'subJob');">설치·정비·생산-인쇄·목재·공예 및 제조 단순</button><input type="hidden" id="mainJob7Nm" value="설치·정비·생산-인쇄·목재·공예 및 제조 단순"><input type="hidden" name="firstJobName" id="jobName12" value="설치·정비·생산-인쇄·목재·공예 및 제조 단순"></li><li><span class="pt08"><input type="checkbox" id="chk10" name="mainJob" title="설치·정비·생산-전기·전자·정보통신 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'10');" value="10"><label for="chk10"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName10" title="설치·정비·생산-전기·전자·정보통신에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('10', 'mainJob8' , 'subJob');">설치·정비·생산-전기·전자·정보통신</button><input type="hidden" id="mainJob8Nm" value="설치·정비·생산-전기·전자·정보통신"><input type="hidden" name="firstJobName" id="jobName10" value="설치·정비·생산-전기·전자·정보통신"></li><li><span class="pt08"><input type="checkbox" id="chk11" name="mainJob" title="설치·정비·생산-화학·환경·섬유·의복·식품가공 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'11');" value="11"><label for="chk11"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName11" title="설치·정비·생산-화학·환경·섬유·의복·식품가공에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('11', 'mainJob9' , 'subJob');">설치·정비·생산-화학·환경·섬유·의복·식품가공</button><input type="hidden" id="mainJob9Nm" value="설치·정비·생산-화학·환경·섬유·의복·식품가공"><input type="hidden" name="firstJobName" id="jobName11" value="설치·정비·생산-화학·환경·섬유·의복·식품가공"></li><li><span class="pt08"><input type="checkbox" id="chk02" name="mainJob" title="연구 및 공학기술 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'02');" value="02"><label for="chk02"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName02" title="연구 및 공학기술에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('02', 'mainJob10' , 'subJob');">연구 및 공학기술</button><input type="hidden" id="mainJob10Nm" value="연구 및 공학기술"><input type="hidden" name="firstJobName" id="jobName02" value="연구 및 공학기술"></li><li><span class="pt08"><input type="checkbox" id="chk07" name="mainJob" title="영업·판매·운전·운송 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'07');" value="07"><label for="chk07"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName07" title="영업·판매·운전·운송에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('07', 'mainJob11' , 'subJob');">영업·판매·운전·운송</button><input type="hidden" id="mainJob11Nm" value="영업·판매·운전·운송"><input type="hidden" name="firstJobName" id="jobName07" value="영업·판매·운전·운송"></li><li><span class="pt08"><input type="checkbox" id="chk05" name="mainJob" title="예술·디자인·방송·스포츠 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'05');" value="05"><label for="chk05"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName05" title="예술·디자인·방송·스포츠에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('05', 'mainJob12' , 'subJob');">예술·디자인·방송·스포츠</button><input type="hidden" id="mainJob12Nm" value="예술·디자인·방송·스포츠"><input type="hidden" name="firstJobName" id="jobName05" value="예술·디자인·방송·스포츠"></li></ul>
										</div>
									</div>
									<div class="col">
										<p class="tit">2차 분류</p>
										<div class="cont_area scroll h280">
											<ul class="box_chk-group chk_row job-search-p" id="subJobDiv"><p class="txt">1차 분류를 선택하세요</p></ul>
										</div>
									</div>
									<div class="col">
										<p class="tit">3차 분류</p>
										<div class="cont_area scroll h280">
											<ul class="box_chk-group chk_row job-search-p" id="thirdJobDiv"><p class="txt">2차 분류를 선택하세요</p></ul>
										</div>
									</div>
								</div>

							</div><!-- virw1 -->
							<div id="wk-jobs-search-view2" style="display: none">
								<div class="list_chk_area only_cont type_col" style="display: block">
									<div class="cont_area" id="wk-jobs-search-content">
									</div>
								</div>
								<span>&nbsp;</span>
								<div>* 분류 리스트로 검색하려면 [분류별보기] 버튼을 클릭하세요.
									<button type="button" class="btn small type02" onclick="viewChange();">분류별 보기</button>
								</div>
							</div>
							<!--// 본문 컨텐츠 -->
							<!-- 버튼 -->
							<a href="#none" class="closed" onclick="fn_show('jobCategory');">
								<span class="blind">팝업 닫기</span>
							</a>
							<!--// 버튼 -->
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">지역</span>
					<div class="cont">
						<div class="layer_more_wrap">
							<div class="layer_btn_wrap">
								<button type="button" class="btn medium type02" onclick="fn_show('jobCatelocation01', 'jobCatelocation02');"><span>지역별</span></button>
								<button type="button" class="btn medium type02" onclick="fn_show('jobCatelocation02', 'jobCatelocation01');"><span>역세권별</span></button>
							</div>
							<div id="jobCatelocation01" style="" class="layer_section on">
								<div class="careers-location-select">
									<div class="box_table_wrap write type03">
										<p class="pop_subtl b1_r">최대 20개의 지역 선택이 가능합니다.</p>

										<!-- table -->
										<table class="box_table mt04">
											<colgroup>
												<col style="width:30%">
												<col>
											</colgroup>
											<tbody>
											<tr>
												<td scope="row" class="pd_none v_top">
													<div class="sort_btn_list">
														<ul>
															<li id="regionOn_00000"><button type="button" onclick="fn_requestRegionSubList('00000');">전체</button></li>
															
																
															
																
																	<li id="regionOn_11000"><button type="button" onclick="fn_requestRegionSubList('11000');">서울</button></li>
																
															
																
																	<li id="regionOn_26000"><button type="button" onclick="fn_requestRegionSubList('26000');">부산</button></li>
																
															
																
																	<li id="regionOn_27000"><button type="button" onclick="fn_requestRegionSubList('27000');">대구</button></li>
																
															
																
																	<li id="regionOn_28000"><button type="button" onclick="fn_requestRegionSubList('28000');">인천</button></li>
																
															
																
																	<li id="regionOn_29000"><button type="button" onclick="fn_requestRegionSubList('29000');">광주</button></li>
																
															
																
																	<li id="regionOn_30000"><button type="button" onclick="fn_requestRegionSubList('30000');">대전</button></li>
																
															
																
																	<li id="regionOn_31000"><button type="button" onclick="fn_requestRegionSubList('31000');">울산</button></li>
																
															
																
																	<li id="regionOn_36110"><button type="button" onclick="fn_requestRegionSubList('36110');">세종</button></li>
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
														</ul>
														<ul>
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
																	<li id="regionOn_41000"><button type="button" onclick="fn_requestRegionSubList('41000');">경기</button></li>
																
															
																
																	<li id="regionOn_43000"><button type="button" onclick="fn_requestRegionSubList('43000');">충북</button></li>
																
															
																
																	<li id="regionOn_44000"><button type="button" onclick="fn_requestRegionSubList('44000');">충남</button></li>
																
															
																
																	<li id="regionOn_46000"><button type="button" onclick="fn_requestRegionSubList('46000');">전남</button></li>
																
															
																
																	<li id="regionOn_47000"><button type="button" onclick="fn_requestRegionSubList('47000');">경북</button></li>
																
															
																
																	<li id="regionOn_48000"><button type="button" onclick="fn_requestRegionSubList('48000');">경남</button></li>
																
															
																
																	<li id="regionOn_50000"><button type="button" onclick="fn_requestRegionSubList('50000');">제주</button></li>
																
															
																
																	<li id="regionOn_51000"><button type="button" onclick="fn_requestRegionSubList('51000');">강원</button></li>
																
															
																
																	<li id="regionOn_52000"><button type="button" onclick="fn_requestRegionSubList('52000');">전북</button></li>
																
															
														</ul>
													</div>
												</td>
												<td class="v_top">
													<div class="ht440px ovflY-scr">
														<div class="box_chk-group flex_al mt0 mb10" id="regionSubDiv">
																<span>
																	<!-- <input type="checkbox">
																	<label for="">전체</label> -->
																</span>
														</div>
													</div>
												</td>
											</tr>
											</tbody>
										</table>
										<!-- //table -->
									</div>
								</div>
								<!-- 버튼 -->
								<a href="#none" class="closed" onclick="fn_show('jobCatelocation01', 'jobCatelocation02');">
									<span class="blind">팝업 닫기</span>
								</a>
								<!--// 버튼 -->
							</div>

							<div id="jobCatelocation02" style="display:none " class="layer_section">
								<div class="box_table_wrap write">
									<div class="box_table_hd">
										<div class="form_box box_sel-group">
											<div class="box_table_group">
												<div class="cell">
													<span class="sel w_xsmall03">
														<select title="지역선택" onchange="fn_changeSubArea(this);" id="staAreaLineInfo1">
															
																<option value="11000">
																	수도권
																</option>
															
																<option value="26000">
																	부산
																</option>
															
																<option value="27000">
																	대구
																</option>
															
																<option value="29000">
																	광주
																</option>
															
																<option value="30000">
																	대전
																</option>
															
														</select>
													</span>
												</div>
											</div>
											<div class="box_table_group">
												<div class="cell">
													<span class="sel w_xsmall03">
														<select title="호선 선택" onchange="fn_changeSubAreaTwo(this);" id="staAreaLineInfo2">
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
																
															
														<option value="11000_1">1호선</option><option value="11000_2">2호선</option><option value="11000_3">3호선</option><option value="11000_4">4호선</option><option value="11000_5">5호선</option><option value="11000_6">6호선</option><option value="11000_7">7호선</option><option value="11000_8">8호선</option><option value="11000_9">9호선</option><option value="11000_11">경의중앙선</option><option value="11000_12">경춘선</option><option value="11000_13">경강</option><option value="11000_14">우이신설</option><option value="11000_15">서해선</option><option value="11000_16">김포골드라인</option><option value="11000_17">신림선</option><option value="11000_21">공항철도</option><option value="11000_31">분당선</option><option value="11000_51">신분당선</option><option value="11000_61">수인선</option><option value="11000_71">의정부경전철</option><option value="11000_81">에버라인</option><option value="11000_91">자기부상</option><option value="28000_1">인천 1호선</option><option value="28000_2">인천 2호선</option></select>
													</span>
												</div>
											</div>
										</div>
									</div>

									<!-- table -->
									<table class="box_table mt16">
										<colgroup>
											<col>
										</colgroup>
										<tbody>
										<tr>
											<td>
												<div class="box_chk-group flex_al col_3 on-scroll" id="checkSubwayList">
												
		<span id="listCheckSubWay_ALL">
			<input type="checkbox" id="checkSubwayALL" name="checkSubway" onclick="f_checkStaArea(this, '전체');" value="11000-1">
			<label for="checkSubwayALL">전체</label>
		</span>
	
		<span id="listCheckSubWay_1">
			<input type="checkbox" id="checkSubway1" name="checkSubway" onclick="f_checkStaArea(this, '가능');" value="11000-1-1">
			<label for="checkSubway1">가능</label>
		</span>
	
		<span id="listCheckSubWay_2">
			<input type="checkbox" id="checkSubway2" name="checkSubway" onclick="f_checkStaArea(this, '가산디지털단지');" value="11000-1-2">
			<label for="checkSubway2">가산디지털단지</label>
		</span>
	
		<span id="listCheckSubWay_3">
			<input type="checkbox" id="checkSubway3" name="checkSubway" onclick="f_checkStaArea(this, '간석');" value="11000-1-3">
			<label for="checkSubway3">간석</label>
		</span>
	
		<span id="listCheckSubWay_4">
			<input type="checkbox" id="checkSubway4" name="checkSubway" onclick="f_checkStaArea(this, '개봉');" value="11000-1-4">
			<label for="checkSubway4">개봉</label>
		</span>
	
		<span id="listCheckSubWay_5">
			<input type="checkbox" id="checkSubway5" name="checkSubway" onclick="f_checkStaArea(this, '관악');" value="11000-1-5">
			<label for="checkSubway5">관악</label>
		</span>
	
		<span id="listCheckSubWay_6">
			<input type="checkbox" id="checkSubway6" name="checkSubway" onclick="f_checkStaArea(this, '광명');" value="11000-1-6">
			<label for="checkSubway6">광명</label>
		</span>
	
		<span id="listCheckSubWay_44">
			<input type="checkbox" id="checkSubway44" name="checkSubway" onclick="f_checkStaArea(this, '광운대');" value="11000-1-44">
			<label for="checkSubway44">광운대</label>
		</span>
	
		<span id="listCheckSubWay_7">
			<input type="checkbox" id="checkSubway7" name="checkSubway" onclick="f_checkStaArea(this, '구로');" value="11000-1-7">
			<label for="checkSubway7">구로</label>
		</span>
	
		<span id="listCheckSubWay_8">
			<input type="checkbox" id="checkSubway8" name="checkSubway" onclick="f_checkStaArea(this, '구일');" value="11000-1-8">
			<label for="checkSubway8">구일</label>
		</span>
	
		<span id="listCheckSubWay_9">
			<input type="checkbox" id="checkSubway9" name="checkSubway" onclick="f_checkStaArea(this, '군포');" value="11000-1-9">
			<label for="checkSubway9">군포</label>
		</span>
	
		<span id="listCheckSubWay_10">
			<input type="checkbox" id="checkSubway10" name="checkSubway" onclick="f_checkStaArea(this, '금정');" value="11000-1-10">
			<label for="checkSubway10">금정</label>
		</span>
	
		<span id="listCheckSubWay_54">
			<input type="checkbox" id="checkSubway54" name="checkSubway" onclick="f_checkStaArea(this, '금천구청');" value="11000-1-54">
			<label for="checkSubway54">금천구청</label>
		</span>
	
		<span id="listCheckSubWay_11">
			<input type="checkbox" id="checkSubway11" name="checkSubway" onclick="f_checkStaArea(this, '남영');" value="11000-1-11">
			<label for="checkSubway11">남영</label>
		</span>
	
		<span id="listCheckSubWay_12">
			<input type="checkbox" id="checkSubway12" name="checkSubway" onclick="f_checkStaArea(this, '노량진');" value="11000-1-12">
			<label for="checkSubway12">노량진</label>
		</span>
	
		<span id="listCheckSubWay_13">
			<input type="checkbox" id="checkSubway13" name="checkSubway" onclick="f_checkStaArea(this, '녹양');" value="11000-1-13">
			<label for="checkSubway13">녹양</label>
		</span>
	
		<span id="listCheckSubWay_14">
			<input type="checkbox" id="checkSubway14" name="checkSubway" onclick="f_checkStaArea(this, '녹천');" value="11000-1-14">
			<label for="checkSubway14">녹천</label>
		</span>
	
		<span id="listCheckSubWay_98">
			<input type="checkbox" id="checkSubway98" name="checkSubway" onclick="f_checkStaArea(this, '당정');" value="11000-1-98">
			<label for="checkSubway98">당정</label>
		</span>
	
		<span id="listCheckSubWay_15">
			<input type="checkbox" id="checkSubway15" name="checkSubway" onclick="f_checkStaArea(this, '대방');" value="11000-1-15">
			<label for="checkSubway15">대방</label>
		</span>
	
		<span id="listCheckSubWay_16">
			<input type="checkbox" id="checkSubway16" name="checkSubway" onclick="f_checkStaArea(this, '덕계');" value="11000-1-16">
			<label for="checkSubway16">덕계</label>
		</span>
	
		<span id="listCheckSubWay_17">
			<input type="checkbox" id="checkSubway17" name="checkSubway" onclick="f_checkStaArea(this, '덕정');" value="11000-1-17">
			<label for="checkSubway17">덕정</label>
		</span>
	
		<span id="listCheckSubWay_18">
			<input type="checkbox" id="checkSubway18" name="checkSubway" onclick="f_checkStaArea(this, '도봉');" value="11000-1-18">
			<label for="checkSubway18">도봉</label>
		</span>
	
		<span id="listCheckSubWay_19">
			<input type="checkbox" id="checkSubway19" name="checkSubway" onclick="f_checkStaArea(this, '도봉산');" value="11000-1-19">
			<label for="checkSubway19">도봉산</label>
		</span>
	
		<span id="listCheckSubWay_20">
			<input type="checkbox" id="checkSubway20" name="checkSubway" onclick="f_checkStaArea(this, '도원');" value="11000-1-20">
			<label for="checkSubway20">도원</label>
		</span>
	
		<span id="listCheckSubWay_21">
			<input type="checkbox" id="checkSubway21" name="checkSubway" onclick="f_checkStaArea(this, '도화');" value="11000-1-21">
			<label for="checkSubway21">도화</label>
		</span>
	
		<span id="listCheckSubWay_22">
			<input type="checkbox" id="checkSubway22" name="checkSubway" onclick="f_checkStaArea(this, '독산');" value="11000-1-22">
			<label for="checkSubway22">독산</label>
		</span>
	
		<span id="listCheckSubWay_23">
			<input type="checkbox" id="checkSubway23" name="checkSubway" onclick="f_checkStaArea(this, '동대문');" value="11000-1-23">
			<label for="checkSubway23">동대문</label>
		</span>
	
		<span id="listCheckSubWay_24">
			<input type="checkbox" id="checkSubway24" name="checkSubway" onclick="f_checkStaArea(this, '동두천');" value="11000-1-24">
			<label for="checkSubway24">동두천</label>
		</span>
	
		<span id="listCheckSubWay_25">
			<input type="checkbox" id="checkSubway25" name="checkSubway" onclick="f_checkStaArea(this, '동두천중앙');" value="11000-1-25">
			<label for="checkSubway25">동두천중앙</label>
		</span>
	
		<span id="listCheckSubWay_26">
			<input type="checkbox" id="checkSubway26" name="checkSubway" onclick="f_checkStaArea(this, '동묘앞');" value="11000-1-26">
			<label for="checkSubway26">동묘앞</label>
		</span>
	
		<span id="listCheckSubWay_27">
			<input type="checkbox" id="checkSubway27" name="checkSubway" onclick="f_checkStaArea(this, '동암');" value="11000-1-27">
			<label for="checkSubway27">동암</label>
		</span>
	
		<span id="listCheckSubWay_28">
			<input type="checkbox" id="checkSubway28" name="checkSubway" onclick="f_checkStaArea(this, '동인천');" value="11000-1-28">
			<label for="checkSubway28">동인천</label>
		</span>
	
		<span id="listCheckSubWay_29">
			<input type="checkbox" id="checkSubway29" name="checkSubway" onclick="f_checkStaArea(this, '두정');" value="11000-1-29">
			<label for="checkSubway29">두정</label>
		</span>
	
		<span id="listCheckSubWay_30">
			<input type="checkbox" id="checkSubway30" name="checkSubway" onclick="f_checkStaArea(this, '망월사');" value="11000-1-30">
			<label for="checkSubway30">망월사</label>
		</span>
	
		<span id="listCheckSubWay_31">
			<input type="checkbox" id="checkSubway31" name="checkSubway" onclick="f_checkStaArea(this, '명학');" value="11000-1-31">
			<label for="checkSubway31">명학</label>
		</span>
	
		<span id="listCheckSubWay_32">
			<input type="checkbox" id="checkSubway32" name="checkSubway" onclick="f_checkStaArea(this, '방학');" value="11000-1-32">
			<label for="checkSubway32">방학</label>
		</span>
	
		<span id="listCheckSubWay_95">
			<input type="checkbox" id="checkSubway95" name="checkSubway" onclick="f_checkStaArea(this, '배방');" value="11000-1-95">
			<label for="checkSubway95">배방</label>
		</span>
	
		<span id="listCheckSubWay_33">
			<input type="checkbox" id="checkSubway33" name="checkSubway" onclick="f_checkStaArea(this, '백운');" value="11000-1-33">
			<label for="checkSubway33">백운</label>
		</span>
	
		<span id="listCheckSubWay_34">
			<input type="checkbox" id="checkSubway34" name="checkSubway" onclick="f_checkStaArea(this, '병점');" value="11000-1-34">
			<label for="checkSubway34">병점</label>
		</span>
	
		<span id="listCheckSubWay_35">
			<input type="checkbox" id="checkSubway35" name="checkSubway" onclick="f_checkStaArea(this, '보산');" value="11000-1-35">
			<label for="checkSubway35">보산</label>
		</span>
	
		<span id="listCheckSubWay_97">
			<input type="checkbox" id="checkSubway97" name="checkSubway" onclick="f_checkStaArea(this, '봉명');" value="11000-1-97">
			<label for="checkSubway97">봉명</label>
		</span>
	
		<span id="listCheckSubWay_36">
			<input type="checkbox" id="checkSubway36" name="checkSubway" onclick="f_checkStaArea(this, '부개');" value="11000-1-36">
			<label for="checkSubway36">부개</label>
		</span>
	
		<span id="listCheckSubWay_37">
			<input type="checkbox" id="checkSubway37" name="checkSubway" onclick="f_checkStaArea(this, '부천');" value="11000-1-37">
			<label for="checkSubway37">부천</label>
		</span>
	
		<span id="listCheckSubWay_38">
			<input type="checkbox" id="checkSubway38" name="checkSubway" onclick="f_checkStaArea(this, '부평');" value="11000-1-38">
			<label for="checkSubway38">부평</label>
		</span>
	
		<span id="listCheckSubWay_96">
			<input type="checkbox" id="checkSubway96" name="checkSubway" onclick="f_checkStaArea(this, '서동탄');" value="11000-1-96">
			<label for="checkSubway96">서동탄</label>
		</span>
	
		<span id="listCheckSubWay_39">
			<input type="checkbox" id="checkSubway39" name="checkSubway" onclick="f_checkStaArea(this, '서울역');" value="11000-1-39">
			<label for="checkSubway39">서울역</label>
		</span>
	
		<span id="listCheckSubWay_40">
			<input type="checkbox" id="checkSubway40" name="checkSubway" onclick="f_checkStaArea(this, '서정리');" value="11000-1-40">
			<label for="checkSubway40">서정리</label>
		</span>
	
		<span id="listCheckSubWay_41">
			<input type="checkbox" id="checkSubway41" name="checkSubway" onclick="f_checkStaArea(this, '석계');" value="11000-1-41">
			<label for="checkSubway41">석계</label>
		</span>
	
		<span id="listCheckSubWay_42">
			<input type="checkbox" id="checkSubway42" name="checkSubway" onclick="f_checkStaArea(this, '석수');" value="11000-1-42">
			<label for="checkSubway42">석수</label>
		</span>
	
		<span id="listCheckSubWay_43">
			<input type="checkbox" id="checkSubway43" name="checkSubway" onclick="f_checkStaArea(this, '성균관대');" value="11000-1-43">
			<label for="checkSubway43">성균관대</label>
		</span>
	
		<span id="listCheckSubWay_45">
			<input type="checkbox" id="checkSubway45" name="checkSubway" onclick="f_checkStaArea(this, '성환');" value="11000-1-45">
			<label for="checkSubway45">성환</label>
		</span>
	
		<span id="listCheckSubWay_46">
			<input type="checkbox" id="checkSubway46" name="checkSubway" onclick="f_checkStaArea(this, '세류');" value="11000-1-46">
			<label for="checkSubway46">세류</label>
		</span>
	
		<span id="listCheckSubWay_47">
			<input type="checkbox" id="checkSubway47" name="checkSubway" onclick="f_checkStaArea(this, '세마');" value="11000-1-47">
			<label for="checkSubway47">세마</label>
		</span>
	
		<span id="listCheckSubWay_48">
			<input type="checkbox" id="checkSubway48" name="checkSubway" onclick="f_checkStaArea(this, '소사');" value="11000-1-48">
			<label for="checkSubway48">소사</label>
		</span>
	
		<span id="listCheckSubWay_49">
			<input type="checkbox" id="checkSubway49" name="checkSubway" onclick="f_checkStaArea(this, '소요산');" value="11000-1-49">
			<label for="checkSubway49">소요산</label>
		</span>
	
		<span id="listCheckSubWay_50">
			<input type="checkbox" id="checkSubway50" name="checkSubway" onclick="f_checkStaArea(this, '송내');" value="11000-1-50">
			<label for="checkSubway50">송내</label>
		</span>
	
		<span id="listCheckSubWay_51">
			<input type="checkbox" id="checkSubway51" name="checkSubway" onclick="f_checkStaArea(this, '송탄');" value="11000-1-51">
			<label for="checkSubway51">송탄</label>
		</span>
	
		<span id="listCheckSubWay_52">
			<input type="checkbox" id="checkSubway52" name="checkSubway" onclick="f_checkStaArea(this, '수원');" value="11000-1-52">
			<label for="checkSubway52">수원</label>
		</span>
	
		<span id="listCheckSubWay_53">
			<input type="checkbox" id="checkSubway53" name="checkSubway" onclick="f_checkStaArea(this, '시청');" value="11000-1-53">
			<label for="checkSubway53">시청</label>
		</span>
	
		<span id="listCheckSubWay_55">
			<input type="checkbox" id="checkSubway55" name="checkSubway" onclick="f_checkStaArea(this, '신길');" value="11000-1-55">
			<label for="checkSubway55">신길</label>
		</span>
	
		<span id="listCheckSubWay_56">
			<input type="checkbox" id="checkSubway56" name="checkSubway" onclick="f_checkStaArea(this, '신도림');" value="11000-1-56">
			<label for="checkSubway56">신도림</label>
		</span>
	
		<span id="listCheckSubWay_57">
			<input type="checkbox" id="checkSubway57" name="checkSubway" onclick="f_checkStaArea(this, '신설동');" value="11000-1-57">
			<label for="checkSubway57">신설동</label>
		</span>
	
		<span id="listCheckSubWay_58">
			<input type="checkbox" id="checkSubway58" name="checkSubway" onclick="f_checkStaArea(this, '신이문');" value="11000-1-58">
			<label for="checkSubway58">신이문</label>
		</span>
	
		<span id="listCheckSubWay_92">
			<input type="checkbox" id="checkSubway92" name="checkSubway" onclick="f_checkStaArea(this, '신창(순천향대)');" value="11000-1-92">
			<label for="checkSubway92">신창(순천향대)</label>
		</span>
	
		<span id="listCheckSubWay_93">
			<input type="checkbox" id="checkSubway93" name="checkSubway" onclick="f_checkStaArea(this, '쌍용(나사렛대)');" value="11000-1-93">
			<label for="checkSubway93">쌍용(나사렛대)</label>
		</span>
	
		<span id="listCheckSubWay_94">
			<input type="checkbox" id="checkSubway94" name="checkSubway" onclick="f_checkStaArea(this, '아산');" value="11000-1-94">
			<label for="checkSubway94">아산</label>
		</span>
	
		<span id="listCheckSubWay_59">
			<input type="checkbox" id="checkSubway59" name="checkSubway" onclick="f_checkStaArea(this, '안양');" value="11000-1-59">
			<label for="checkSubway59">안양</label>
		</span>
	
		<span id="listCheckSubWay_60">
			<input type="checkbox" id="checkSubway60" name="checkSubway" onclick="f_checkStaArea(this, '양주');" value="11000-1-60">
			<label for="checkSubway60">양주</label>
		</span>
	
		<span id="listCheckSubWay_61">
			<input type="checkbox" id="checkSubway61" name="checkSubway" onclick="f_checkStaArea(this, '역곡');" value="11000-1-61">
			<label for="checkSubway61">역곡</label>
		</span>
	
		<span id="listCheckSubWay_101">
			<input type="checkbox" id="checkSubway101" name="checkSubway" onclick="f_checkStaArea(this, '연천');" value="11000-1-101">
			<label for="checkSubway101">연천</label>
		</span>
	
		<span id="listCheckSubWay_62">
			<input type="checkbox" id="checkSubway62" name="checkSubway" onclick="f_checkStaArea(this, '영등포');" value="11000-1-62">
			<label for="checkSubway62">영등포</label>
		</span>
	
		<span id="listCheckSubWay_63">
			<input type="checkbox" id="checkSubway63" name="checkSubway" onclick="f_checkStaArea(this, '오류동');" value="11000-1-63">
			<label for="checkSubway63">오류동</label>
		</span>
	
		<span id="listCheckSubWay_64">
			<input type="checkbox" id="checkSubway64" name="checkSubway" onclick="f_checkStaArea(this, '오산');" value="11000-1-64">
			<label for="checkSubway64">오산</label>
		</span>
	
		<span id="listCheckSubWay_65">
			<input type="checkbox" id="checkSubway65" name="checkSubway" onclick="f_checkStaArea(this, '오산대');" value="11000-1-65">
			<label for="checkSubway65">오산대</label>
		</span>
	
		<span id="listCheckSubWay_66">
			<input type="checkbox" id="checkSubway66" name="checkSubway" onclick="f_checkStaArea(this, '온수');" value="11000-1-66">
			<label for="checkSubway66">온수</label>
		</span>
	
		<span id="listCheckSubWay_91">
			<input type="checkbox" id="checkSubway91" name="checkSubway" onclick="f_checkStaArea(this, '온양온천');" value="11000-1-91">
			<label for="checkSubway91">온양온천</label>
		</span>
	
		<span id="listCheckSubWay_67">
			<input type="checkbox" id="checkSubway67" name="checkSubway" onclick="f_checkStaArea(this, '외대앞');" value="11000-1-67">
			<label for="checkSubway67">외대앞</label>
		</span>
	
		<span id="listCheckSubWay_68">
			<input type="checkbox" id="checkSubway68" name="checkSubway" onclick="f_checkStaArea(this, '용산');" value="11000-1-68">
			<label for="checkSubway68">용산</label>
		</span>
	
		<span id="listCheckSubWay_69">
			<input type="checkbox" id="checkSubway69" name="checkSubway" onclick="f_checkStaArea(this, '월계');" value="11000-1-69">
			<label for="checkSubway69">월계</label>
		</span>
	
		<span id="listCheckSubWay_70">
			<input type="checkbox" id="checkSubway70" name="checkSubway" onclick="f_checkStaArea(this, '의왕');" value="11000-1-70">
			<label for="checkSubway70">의왕</label>
		</span>
	
		<span id="listCheckSubWay_71">
			<input type="checkbox" id="checkSubway71" name="checkSubway" onclick="f_checkStaArea(this, '의정부');" value="11000-1-71">
			<label for="checkSubway71">의정부</label>
		</span>
	
		<span id="listCheckSubWay_72">
			<input type="checkbox" id="checkSubway72" name="checkSubway" onclick="f_checkStaArea(this, '인천');" value="11000-1-72">
			<label for="checkSubway72">인천</label>
		</span>
	
		<span id="listCheckSubWay_100">
			<input type="checkbox" id="checkSubway100" name="checkSubway" onclick="f_checkStaArea(this, '전곡');" value="11000-1-100">
			<label for="checkSubway100">전곡</label>
		</span>
	
		<span id="listCheckSubWay_73">
			<input type="checkbox" id="checkSubway73" name="checkSubway" onclick="f_checkStaArea(this, '제기동');" value="11000-1-73">
			<label for="checkSubway73">제기동</label>
		</span>
	
		<span id="listCheckSubWay_74">
			<input type="checkbox" id="checkSubway74" name="checkSubway" onclick="f_checkStaArea(this, '제물포');" value="11000-1-74">
			<label for="checkSubway74">제물포</label>
		</span>
	
		<span id="listCheckSubWay_75">
			<input type="checkbox" id="checkSubway75" name="checkSubway" onclick="f_checkStaArea(this, '종각');" value="11000-1-75">
			<label for="checkSubway75">종각</label>
		</span>
	
		<span id="listCheckSubWay_76">
			<input type="checkbox" id="checkSubway76" name="checkSubway" onclick="f_checkStaArea(this, '종로3가');" value="11000-1-76">
			<label for="checkSubway76">종로3가</label>
		</span>
	
		<span id="listCheckSubWay_77">
			<input type="checkbox" id="checkSubway77" name="checkSubway" onclick="f_checkStaArea(this, '종로5가');" value="11000-1-77">
			<label for="checkSubway77">종로5가</label>
		</span>
	
		<span id="listCheckSubWay_78">
			<input type="checkbox" id="checkSubway78" name="checkSubway" onclick="f_checkStaArea(this, '주안');" value="11000-1-78">
			<label for="checkSubway78">주안</label>
		</span>
	
		<span id="listCheckSubWay_79">
			<input type="checkbox" id="checkSubway79" name="checkSubway" onclick="f_checkStaArea(this, '중동');" value="11000-1-79">
			<label for="checkSubway79">중동</label>
		</span>
	
		<span id="listCheckSubWay_80">
			<input type="checkbox" id="checkSubway80" name="checkSubway" onclick="f_checkStaArea(this, '지제');" value="11000-1-80">
			<label for="checkSubway80">지제</label>
		</span>
	
		<span id="listCheckSubWay_81">
			<input type="checkbox" id="checkSubway81" name="checkSubway" onclick="f_checkStaArea(this, '지행');" value="11000-1-81">
			<label for="checkSubway81">지행</label>
		</span>
	
		<span id="listCheckSubWay_82">
			<input type="checkbox" id="checkSubway82" name="checkSubway" onclick="f_checkStaArea(this, '직산');" value="11000-1-82">
			<label for="checkSubway82">직산</label>
		</span>
	
		<span id="listCheckSubWay_83">
			<input type="checkbox" id="checkSubway83" name="checkSubway" onclick="f_checkStaArea(this, '진위');" value="11000-1-83">
			<label for="checkSubway83">진위</label>
		</span>
	
		<span id="listCheckSubWay_84">
			<input type="checkbox" id="checkSubway84" name="checkSubway" onclick="f_checkStaArea(this, '창동');" value="11000-1-84">
			<label for="checkSubway84">창동</label>
		</span>
	
		<span id="listCheckSubWay_85">
			<input type="checkbox" id="checkSubway85" name="checkSubway" onclick="f_checkStaArea(this, '천안');" value="11000-1-85">
			<label for="checkSubway85">천안</label>
		</span>
	
		<span id="listCheckSubWay_86">
			<input type="checkbox" id="checkSubway86" name="checkSubway" onclick="f_checkStaArea(this, '청량리');" value="11000-1-86">
			<label for="checkSubway86">청량리</label>
		</span>
	
		<span id="listCheckSubWay_102">
			<input type="checkbox" id="checkSubway102" name="checkSubway" onclick="f_checkStaArea(this, '청산');" value="11000-1-102">
			<label for="checkSubway102">청산</label>
		</span>
	
		<span id="listCheckSubWay_99">
			<input type="checkbox" id="checkSubway99" name="checkSubway" onclick="f_checkStaArea(this, '탕정역');" value="11000-1-99">
			<label for="checkSubway99">탕정역</label>
		</span>
	
		<span id="listCheckSubWay_87">
			<input type="checkbox" id="checkSubway87" name="checkSubway" onclick="f_checkStaArea(this, '평택');" value="11000-1-87">
			<label for="checkSubway87">평택</label>
		</span>
	
		<span id="listCheckSubWay_88">
			<input type="checkbox" id="checkSubway88" name="checkSubway" onclick="f_checkStaArea(this, '화서');" value="11000-1-88">
			<label for="checkSubway88">화서</label>
		</span>
	
		<span id="listCheckSubWay_89">
			<input type="checkbox" id="checkSubway89" name="checkSubway" onclick="f_checkStaArea(this, '회기');" value="11000-1-89">
			<label for="checkSubway89">회기</label>
		</span>
	
		<span id="listCheckSubWay_90">
			<input type="checkbox" id="checkSubway90" name="checkSubway" onclick="f_checkStaArea(this, '회룡');" value="11000-1-90">
			<label for="checkSubway90">회룡</label>
		</span>
	</div>
											</td>
										</tr>
										</tbody>
									</table>
									<!-- //table -->
								</div>

								<!-- 버튼 -->
								<a href="#none" class="closed" onclick="fn_show('jobCatelocation02', 'jobCatelocation01');">
									<span class="blind">팝업 닫기</span>
								</a>
								<!--// 버튼 -->
							</div>
						</div>
					</div>
				</li>

				<li>
					<span class="tit b1_sb">경력</span>
					<div class="cont">
						<div class="box_table_group has_date_input">
							<div class="cell_wrap">
								<div class="box_chk-group">
									<span>
										<input type="checkbox" id="careerTypeA" name="careerType" value="" onclick="fnCareerCheck('A');" checked="checked">
										<label for="careerTypeA">전체</label>
									</span>
									<span>
										<input type="checkbox" id="careerTypeN" name="careerType" value="N" onclick="fnCareerCheck('N');">
										<label for="careerTypeN">신입</label>
									</span>
									<span>
										<input type="checkbox" id="careerTypeE" name="careerType" value="E" onclick="fnCareerCheck('E');">
										<label for="careerTypeE">경력</label>
									</span>
								</div>
								<span class="box_int_txt ml16">( </span>
								<span class="box_ipt ml08">
									<input type="text" class="input_txt type_small" title="최소 경력(년)을 입력해주세요." id="careerFromParam" onkeyup="input_limit_string(this,'/d');" onblur="input_limit_string(this,'/d');" name="careerFromParam" maxlength="3" value="" disabled="disabled" placeholder="">
								</span>
								<span class="box_int_txt"> 년 ~</span>
								<span class="box_ipt ml08">
									<input type="text" class="input_txt type_small" title="최대 경력(년)을 입력해주세요." id="careerToParam" onkeyup="input_limit_string(this,'/d');" onblur="input_limit_string(this,'/d');" name="careerToParam" maxlength="3" value="" disabled="disabled" placeholder="">
								</span>
								<span class="box_int_txt"> 년)</span>
								<div class="box_chk-group ml08">
									<span>
										<input type="checkbox" id="careerTypeZ" name="careerType" value="Z" onclick="fnCareerCheck('Z');">
										<label for="careerTypeZ">관계없음</label>
									</span>
								</div>
							</div>
						</div>
					</div>
				</li>

				<li>
					<span class="tit b1_sb">고용24 입사지원</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" id="emailApplyYnParamY" name="emailApplyYnParam" value="Y" onclick="resultCheckBoxTemplate('emailApplyYnParam');">
								<label for="emailApplyYnParamY">고용24 입사지원 가능</label>
							</span>
						</div>
					</div>
				</li>
			</ul>

			<ul class="slide_cont">

				<li>
					<span class="tit b1_sb">재택근무 가능 여부</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" id="tlmgYnParamY" name="tlmgYnParam" value="Y" onclick="resultCheckBoxTemplate('tlmgYnParam');">
								<label for="tlmgYnParamY">재택근무</label>
							</span>
						</div>
					</div>
				</li>

				<li>
					<span class="tit b1_sb">학력</span>
					<div class="cont">
						<div class="box_chk-group list_type">
                        	<span>
								<input type="checkbox" id="b_academicGbnoEdu" name="b_academicGbnoEdu" value="noEdu" onclick="fn_academicGbn('b_academicGbnoEdu');" checked="checked">
								<label for="b_academicGbnoEdu">전체</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn02" name="b_academicGbn" value="01,02" onclick="fn_academicGbn('b_academicGbn02');">
								<label for="b_academicGbn02">중졸이하</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn03" name="b_academicGbn" value="03" onclick="fn_academicGbn('b_academicGbn03');">
								<label for="b_academicGbn03">고졸</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn04" name="b_academicGbn" value="04" onclick="fn_academicGbn('b_academicGbn04');">
								<label for="b_academicGbn04">대졸(2~3년)</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn05" name="b_academicGbn" value="05" onclick="fn_academicGbn('b_academicGbn05');">
								<label for="b_academicGbn05">대졸(4년)</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn06" name="b_academicGbn" value="06" onclick="fn_academicGbn('b_academicGbn06');">
								<label for="b_academicGbn06">석사</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn07" name="b_academicGbn" value="07" onclick="fn_academicGbn('b_academicGbn07');">
								<label for="b_academicGbn07">박사</label>
							</span>
							<span>
								<input type="checkbox" id="b_academicGbn00" name="b_academicGbn" value="00" onclick="fn_academicGbn('b_academicGbn00');">
								<label for="b_academicGbn00">학력무관</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">고용형태
						<div class="box_tooltip">
							<button type="button" class="btn_help dis"><span class="blind">도움말</span></button>
							<div class="box_help-data w_big">
                                <p class="txt_list"><strong>고용 형태</strong></p>
                                <p class="txt_list"><strong>기간의 정함이 없는 근로계약</strong> : 근로계약을 명시하지 않고 계약하는 일자리, 무기계약직 혹은 정규직 일자리 등</p>
                                <p class="txt_list"><strong>기간의 정함이 있는 근로계약</strong> : 근로기간을 정하여 계약하는 일자리, 계약직 등</p>
                                <p class="txt_list"><strong>시간선택제 일자리</strong> : 전일제 근로자보다 짧게 일하지만, 근로조건 등은 차별이 없는 일자리</p>
                                <p class="txt_list"><strong>파견근로</strong> : 파견사업주(A)에게 고용되었으나, 사용사업주(B)의 사업체에 파견하여 근로하는 것으로, 임금이나 신분상의 고용관계는 파견사업주(A)의 관리를 받지만, 업무상 지휘, 명령은 사용업체(B)로부터 받게 되는 근로형태</p>
                                <p class="txt_list"><strong>대체인력</strong> : 출산전후휴가, 육아휴직 등에 있는 근로자를 대신하여 한정된 기간 동안 근무하는 자</p>
                                <button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span></button>
                            </div>
						</div>
					</span>
					<div class="cont">
						<div class="box_chk-group flex_al col_2">
							
									
									<span>
										<input type="checkbox" id="employGbnParam10" name="employGbnParam" value="10" onclick="resultCheckBoxTemplate('employGbnParam');f_empTypeChecked(this);">
										
											
											
											
												<label for="employGbnParam10">기간의 정함이 없는 근로계약</label>
											
										
									</span>
								
							
									
									<span>
										<input type="checkbox" id="employGbnParam11" name="employGbnParam" value="11" onclick="resultCheckBoxTemplate('employGbnParam');f_empTypeChecked(this);">
										
											
											
											
												<label for="employGbnParam11">기간의 정함이 없는 근로계약(시간(선택)제)</label>
											
										
									</span>
								
							
									
									<span>
										<input type="checkbox" id="employGbnParam20" name="employGbnParam" value="20" onclick="resultCheckBoxTemplate('employGbnParam');f_empTypeChecked(this);">
										
											
											
											
												<label for="employGbnParam20">기간의 정함이 있는 근로계약</label>
											
										
									</span>
								
							
									
									<span>
										<input type="checkbox" id="employGbnParam21" name="employGbnParam" value="21" onclick="resultCheckBoxTemplate('employGbnParam');f_empTypeChecked(this);">
										
											
											
											
												<label for="employGbnParam21">기간의 정함이 있는 근로계약(시간(선택)제)</label>
											
										
									</span>
								
							
									
									<span>
										<input type="checkbox" id="employGbnParam4" name="employGbnParam" value="4" onclick="resultCheckBoxTemplate('employGbnParam');f_empTypeChecked(this);">
										
											
											
											
												<label for="employGbnParam4">파견근로</label>
											
										
									</span>
								
							
								
							
								
							
							<span>
								<input type="checkbox" id="subEmpHopeYnParamY" name="subEmpHopeYnParam" onclick="resultCheckBoxTemplate('subEmpHopeYnParam');" value="Y">
								<label for="subEmpHopeYnParamY">대체인력채용</label>
							</span>
						</div>
						<div class="mt10" id="termContractMmcntSpan" style="display: none">
							<p class="reset"><strong class="font-black">근무기간</strong></p>
							<div class="label-wrap line-0">
								<span>
									<input type="checkbox" class="input_chk" id="termContractMmcntParam1" onclick="resultCheckBoxTemplate('termContractMmcntParam');" name="termContractMmcntParam" value="1"> <label for="termContractMmcntParam1">근무기간 1~3개월</label>
								</span>
								<span>
									<input type="checkbox" class="input_chk" id="termContractMmcntParam3" onclick="resultCheckBoxTemplate('termContractMmcntParam');" name="termContractMmcntParam" value="3"> <label for="termContractMmcntParam3">근무기간 3~6개월</label>
								</span>
								<span>
									<input type="checkbox" class="input_chk" id="termContractMmcntParam6" onclick="resultCheckBoxTemplate('termContractMmcntParam');" name="termContractMmcntParam" value="6"> <label for="termContractMmcntParam6">근무기간 6~12개월</label>
								</span>
								<span>
									<input type="checkbox" class="input_chk" id="termContractMmcntParam12" onclick="resultCheckBoxTemplate('termContractMmcntParam');" name="termContractMmcntParam" value="12"> <label for="termContractMmcntParam12">근무기간 12개월 이상</label>
								</span>
							</div>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">희망임금</span>
					<div class="cont">
						<div class="box_table_group">
							<div class="cell_wrap mo_style">
								<div class="mo_block">
                                	<span class="sel w_xsmall02">
										<select title="희망임금 단위 선택" onchange="fn_PayType(this.options[this.selectedIndex].value)" id="salSelect">
											<option value="">선택</option>
											
												<option value="Y">
													연봉
												</option>
											
												<option value="M">
													월급
												</option>
											
												<option value="D">
													일급
												</option>
											
												<option value="H">
													시급
												</option>
											
										</select>
									</span>
								</div>
								<div class="mo_block">
                                	<span class="box_ipt w_xsmall02">
										<input type="text" class="input_txt medium" id="b_minPay" name="b_minPay" onkeyup="input_limit_string(this,'/d');" onblur="input_limit_string(this,'/d');" maxlength="6" disabled="" value="" title="희망임금 최소를 입력해 주세요.">
									</span>
									<span class="box_int_txt" id="minPayTitle">만원이상 ~</span>
									<span class="box_ipt w_xsmall02 ml08">
										<input type="text" class="input_txt medium" id="b_maxPay" name="b_maxPay" onkeyup="input_limit_string(this,'/d');" onblur="input_limit_string(this,'/d');" maxlength="6" value="" disabled="" title="희망임금 최고를 입력해 주세요.">
									</span>
									<span class="box_int_txt" id="maxPayTitle">만원이하</span>
								</div>
							</div>
							<div class="cell_wrap mo_style mt08">
								<div class="mo_block">
									<div class="box_chk-group">
                                    	<span>
											<input type="checkbox" id="noPayType" onclick="fnPayType('');">
											<label for="noPayType">관계없음</label>
										</span>
										<!-- <span>
											<input type="checkbox">
											<label for="">면접 후 결정 가능</label>
										</span> -->
									</div>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">기업형태</span>
					<div class="cont">
						<div class="box_chk-group flex_al">
							<span>
								<input type="checkbox" id="enterPriseGbnParamall" name="enterPriseGbnParam" value="" onclick="fnEnterPriseGbnAll('all');" checked="checked">
								<label for="enterPriseGbnParamall">전체</label>
							</span>
							
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam01" name="enterPriseGbnParam" value="01" onclick="fnEnterPriseGbnAll('1');">
										<label for="enterPriseGbnParam01">대기업</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam04" name="enterPriseGbnParam" value="04" onclick="fnEnterPriseGbnAll('2');">
										<label for="enterPriseGbnParam04">공무원/공기업/공공기관</label>
									</span>
								
							
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam05" name="enterPriseGbnParam" value="05" onclick="fnEnterPriseGbnAll('4');">
										<label for="enterPriseGbnParam05">외국계기업</label>
									</span>
								
							
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam06" name="enterPriseGbnParam" value="06" onclick="fnEnterPriseGbnAll('6');">
										<label for="enterPriseGbnParam06">코스피</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam07" name="enterPriseGbnParam" value="07" onclick="fnEnterPriseGbnAll('7');">
										<label for="enterPriseGbnParam07">코스닥</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam09" name="enterPriseGbnParam" value="09" onclick="fnEnterPriseGbnAll('8');">
										<label for="enterPriseGbnParam09">일학습병행기업</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam10" name="enterPriseGbnParam" value="10" onclick="fnEnterPriseGbnAll('9');">
										<label for="enterPriseGbnParam10">청년친화강소기업</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam11" name="enterPriseGbnParam" value="11" onclick="fnEnterPriseGbnAll('10');">
										<label for="enterPriseGbnParam11">가족친화인증기업</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="enterPriseGbnParam20" name="enterPriseGbnParam" value="20" onclick="fnEnterPriseGbnAll('11');">
										<label for="enterPriseGbnParam20">중견기업</label>
									</span>
								
							
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">채용구분</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" id="empTpGbcdParam1" name="empTpGbcdParam" value="1" onclick="resultCheckBoxTemplate('empTpGbcdParam');" checked="checked">
								<label for="empTpGbcdParam1">상용직</label>
							</span>
							<span>
								<input type="checkbox" id="empTpGbcdParam2" name="empTpGbcdParam" value="2" onclick="resultCheckBoxTemplate('empTpGbcdParam');">
								<label for="empTpGbcdParam2">일용직</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">근무형태</span>
					<div class="cont">
						<div class="box_chk-group">
							
								
								<span>
									<input type="checkbox" id="holidayGbnParam1" onclick="resultCheckBoxTemplate('holidayGbnParam')" name="holidayGbnParam" value="1">
									<label for="holidayGbnParam1">주 5일 </label>
								</span>
								
							
								
								<span>
									<input type="checkbox" id="holidayGbnParam2" onclick="resultCheckBoxTemplate('holidayGbnParam')" name="holidayGbnParam" value="2">
									<label for="holidayGbnParam2">주 6일 </label>
								</span>
								
							
								
								<span>
									<input type="checkbox" id="holidayGbnParam4" onclick="resultCheckBoxTemplate('holidayGbnParam')" name="holidayGbnParam" value="4">
									<label for="holidayGbnParam4">주 4일 </label>
								</span>
								
							
								
								<span>
									<input type="checkbox" id="holidayGbnParam5" onclick="resultCheckBoxTemplate('holidayGbnParam')" name="holidayGbnParam" value="5">
									<label for="holidayGbnParam5">주 3일 </label>
								</span>
								
							
								
								<span>
									<input type="checkbox" id="holidayGbnParam6" onclick="resultCheckBoxTemplate('holidayGbnParam')" name="holidayGbnParam" value="6">
									<label for="holidayGbnParam6">주 2일 </label>
								</span>
								
							
								
								<span>
									<input type="checkbox" id="holidayGbnParam7" onclick="resultCheckBoxTemplate('holidayGbnParam')" name="holidayGbnParam" value="7">
									<label for="holidayGbnParam7">주 1일 </label>
								</span>
								
							
								
							
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">격일근무 여부</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" id="eodwYnParamY" name="eodwYnParam" value="Y" onclick="resultCheckBoxTemplate('eodwYnParam');">
								<label for="eodwYnParamY">격일근무</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">근로시간단축 여부</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" name="laborHrShortYnParam" id="laborHrShortYnParamY" value="Y" onclick="resultCheckBoxTemplate('laborHrShortYnParam');">
								<label for="laborHrShortYnParamY">근로시간단축여부</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">교대근무여부</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" id="shsyWorkSecdParamY" name="shsyWorkSecdParam" value="Y" onclick="resultCheckBoxTemplate('shsyWorkSecdParam');">
								<label for="shsyWorkSecdParamY">교대근무가능여부</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">식사(비)제공</span>
					<div class="cont">
						<div class="box_chk-group">
							
								
									<span>
										<input type="checkbox" id="mealOfferClcdParam1" name="mealOfferClcdParam" value="1" onclick="resultCheckBoxTemplate('mealOfferClcdParam')">
										<label for="mealOfferClcdParam1">1식</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="mealOfferClcdParam2" name="mealOfferClcdParam" value="2" onclick="resultCheckBoxTemplate('mealOfferClcdParam')">
										<label for="mealOfferClcdParam2">2식</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="mealOfferClcdParam3" name="mealOfferClcdParam" value="3" onclick="resultCheckBoxTemplate('mealOfferClcdParam')">
										<label for="mealOfferClcdParam3">3식</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" id="mealOfferClcdParam5" name="mealOfferClcdParam" value="5" onclick="resultCheckBoxTemplate('mealOfferClcdParam')">
										<label for="mealOfferClcdParam5">중식비지급</label>
									</span>
								
							
								
							
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">기타 복리후생
						<div class="box_tooltip">
							<button type="button" class="btn_help"><span class="blind">도움말</span></button>
							<div class="box_help-data w_big">
								<ul class="box_list_area">
									<li class="txt_list">AND : 선택된 항목이 모두 포함된 결과값을 검색</li>
									<li class="txt_list">OR : 선택된 항목 중 하나 이상 포함된 결과값을 검색</li>
								</ul>
								<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span></button>
							</div>
						</div>
						<br>
						<span class="switch type2">

							<input type="checkbox" name="switch4" id="switch4" onclick="fn_etcBenefit(this);">
							<label for="switch4">
								<span class="slider">
									<span class="no_txt">OR</span>
									<span class="on_txt">AND</span>
								</span>
							</label>
						</span>
					</span>
					<div class="cont">
						<div class="box_chk-group list_type">
							
								<span>
									<input type="checkbox" id="b_benefitGbn02" name="b_benefitGbn" value="02" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn02">통근버스</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn01" name="b_benefitGbn" value="01" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn01">기숙사</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn11" name="b_benefitGbn" value="11" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn11">차량유지비</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn12" name="b_benefitGbn" value="12" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn12">교육비 지원</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn13" name="b_benefitGbn" value="13" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn13">자녀 학자금 지원</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn06" name="b_benefitGbn" value="06" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn06">주택자금 지원</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn10" name="b_benefitGbn" value="10" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn10">직원대출 제도</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn14" name="b_benefitGbn" value="14" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn14">모성보호시설</label>
								</span>
							
								<span>
									<input type="checkbox" id="b_benefitGbn09" name="b_benefitGbn" value="09" onclick="resultCheckBoxTemplate('b_benefitGbn');">
									<label for="b_benefitGbn09">기타</label>
								</span>
							
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">장애인 희망채용</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" id="disableEmpHopeGbnParamY" name="disableEmpHopeGbnParam" value="Y" onclick="f_disableEmpHopeANDEtcDisable('1');resultCheckBoxTemplate('disableEmpHopeGbnParam');">
								<label for="disableEmpHopeGbnParamY">장애인 병행채용</label>
							</span>
							<span>
								<input type="checkbox" id="disableEmpHopeGbnParamD" name="disableEmpHopeGbnParam" value="D" onclick="resultCheckBoxTemplate('disableEmpHopeGbnParam');">
								<label for="disableEmpHopeGbnParamD">장애인만 채용</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">병역 특례</span>
					<div class="cont">
						<div class="box_chk-group">
                        	<span>
								<input type="checkbox" name="actServExcYnParam" id="actServExcYnParamY" value="Y" onclick="resultCheckBoxTemplate('actServExcYnParam');">
								<label for="actServExcYnParamY">현역병 입영대상자</label>
							</span>

							<span>
								<input type="checkbox" name="resrDutyExcYnParam" id="resrDutyExcYnParamY" value="Y" onclick="resultCheckBoxTemplate('resrDutyExcYnParam');">
								<label for="resrDutyExcYnParamY">보충역 대상자</label>
							</span>

							<span>
								<input type="checkbox" name="infaYnParam" id="infaYnParamY" value="Y" onclick="resultCheckBoxTemplate('infaYnParam');">
								<label for="infaYnParamY">산업기능 요원</label>
							</span>
							<span>
								<input type="checkbox" name="publDutyExcYnParam" id="publDutyExcYnParamY" value="Y" onclick="resultCheckBoxTemplate('publDutyExcYnParam');">
								<label for="publDutyExcYnParamY">전문연구 요원</label>
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">자격면허</span>
					<div class="cont">
						<div class="box_table_group">
							<div class="cell_wrap">
								<button type="button" class="btn medium type02" onclick="fn_show('jobLicense');"><span>자격증 선택</span></button>
								<div class="box_chk-group ml16">
									<span>
										<input type="checkbox" name="b_essCertChk" id="b_essCertChkY" value="Y" onclick="onEssCertlabelChk();resultCheckBoxTemplate('b_essCertChk');">
										<label for="b_essCertChkY">필수자격만 검색</label>
									</span>
								</div>
							</div>
						</div>
						<div id="jobLicense" style="display:none " class="layer_section">
							<!-- 본문 컨텐츠 -->
							<div class="cont mt16">
								<!-- 250416 article 태그 삭제 -->
								<table class="search_table"><caption>자격면허찾기을(를) 제공하는 표</caption>
									
									<colgroup>
										<col style="width:20%;">
										<col>
									</colgroup>
									<tbody>
									<tr>
										<th scope="row"><span>자격면허찾기</span></th>
										<td>
											<div class="box_sch_group">
													<span class="box_ipt">
														<input type="text" class="input_txt" id="licSearchTxt" onkeypress="if(event.keyCode==13) fn_LicSearch('list');" title="자격면허를 입력해 주세요." placeholder="자격증 관련 키워드를 입력하세요. 예) 영업, 운전, 사무직">
														<button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
													</span>
												<button type="button" class="btn medium fill type01" onclick="fn_LicSearch('list');">검색</button>
											</div>
										</td>
									</tr>
									</tbody>
								</table>

								<div class="tab_wrap bg_type mt24" data-role="tab" id="licBtnList">
									<ul class="tab_title" role="tablist">
										<li aria-controls="tab-panel-01" class="active"><button type="button" role="tab" aria-selected="true" onclick="fn_tabChngLic(this, 0, '50000');"><span>국가기술자격</span></button></li> <!-- D: 활성화시 class[active] add -->
										<li aria-controls="tab-panel-02"><button type="button" role="tab" aria-selected="false" onclick="fn_tabChngLic(this, 1, '60000');" "=""><span>국가전문자격</span></button></li>
										<!-- 2023-10-31 요청사항으로 공인민간자격 삭제 -->
										<!-- <li aria-controls="tab-panel-03"><button type="button" role="tab" aria-selected="false" onclick="fn_tabChngLic(this, 2, '70000');""><span>공인민간자격</span></button></li> -->
									</ul>
									<div class="tab_cont">

										<div id="tab-panel-01" class="box_tab-contents active" role="tabpanel">
											<div class="btn_search_korean">
												
													
														<button onclick="fn_SelLicMain(0, '50001', this);" type="button" class="btn small type02  active" title="선택됨">ㄱ</button>
													
												
													
														<button onclick="fn_SelLicMain(1, '50002', this);" type="button" class="btn small type02 ">ㄴ</button>
													
												
													
														<button onclick="fn_SelLicMain(2, '50003', this);" type="button" class="btn small type02 ">ㄷ</button>
													
												
													
														<button onclick="fn_SelLicMain(3, '50004', this);" type="button" class="btn small type02 ">ㄹ</button>
													
												
													
														<button onclick="fn_SelLicMain(4, '50005', this);" type="button" class="btn small type02 ">ㅁ</button>
													
												
													
														<button onclick="fn_SelLicMain(5, '50006', this);" type="button" class="btn small type02 ">ㅂ</button>
													
												
													
														<button onclick="fn_SelLicMain(6, '50007', this);" type="button" class="btn small type02 ">ㅅ</button>
													
												
													
														<button onclick="fn_SelLicMain(7, '50008', this);" type="button" class="btn small type02 ">ㅇ</button>
													
												
													
														<button onclick="fn_SelLicMain(8, '50009', this);" type="button" class="btn small type02 ">ㅈ</button>
													
												
													
														<button onclick="fn_SelLicMain(9, '50010', this);" type="button" class="btn small type02 ">ㅊ</button>
													
												
													
														<button onclick="fn_SelLicMain(10, '50011', this);" type="button" class="btn small type02 ">ㅋ</button>
													
												
													
														<button onclick="fn_SelLicMain(11, '50012', this);" type="button" class="btn small type02 ">ㅌ</button>
													
												
													
														<button onclick="fn_SelLicMain(12, '50013', this);" type="button" class="btn small type02 ">ㅍ</button>
													
												
													
														<button onclick="fn_SelLicMain(13, '50014', this);" type="button" class="btn small type02 ">ㅎ</button>
													
												
													
														<button onclick="fn_SelLicMain(14, '50090', this);" type="button" class="btn small type02 ">기타</button>
													
												
													
												
													
												
											</div>

											<div class="list_chk_area only_cont">
												<div class="cont_area mt16">
													<div class="box_chk-group flex_al col_3" id="lic_5">
		<span>
	<label for="licItem5009434"><input type="checkbox" id="licItem5009434" name="licItem" onclick="fnCheckItem('5009434', '가구도장기능사보', 'lic', this)"> 가구도장기능사보</label>
</span>
	
		<span>
	<label for="licItem5005776"><input type="checkbox" id="licItem5005776" name="licItem" onclick="fnCheckItem('5005776', '가구도장산업기사', 'lic', this)"> 가구도장산업기사</label>
</span>
	
		<span>
	<label for="licItem5007140"><input type="checkbox" id="licItem5007140" name="licItem" onclick="fnCheckItem('5007140', '가구제작기능사', 'lic', this)"> 가구제작기능사</label>
</span>
	
		<span>
	<label for="licItem5008900"><input type="checkbox" id="licItem5008900" name="licItem" onclick="fnCheckItem('5008900', '가구제작기능사보', 'lic', this)"> 가구제작기능사보</label>
</span>
	
		<span>
	<label for="licItem5002142"><input type="checkbox" id="licItem5002142" name="licItem" onclick="fnCheckItem('5002142', '가구제작산업기사', 'lic', this)"> 가구제작산업기사</label>
</span>
	
		<span>
	<label for="licItem5007909"><input type="checkbox" id="licItem5007909" name="licItem" onclick="fnCheckItem('5007909', '가눈섭기능사', 'lic', this)"> 가눈섭기능사</label>
</span>
	
		<span>
	<label for="licItem5009459"><input type="checkbox" id="licItem5009459" name="licItem" onclick="fnCheckItem('5009459', '가눈섭기능사보', 'lic', this)"> 가눈섭기능사보</label>
</span>
	
		<span>
	<label for="licItem5009458"><input type="checkbox" id="licItem5009458" name="licItem" onclick="fnCheckItem('5009458', '가발기능사보', 'lic', this)"> 가발기능사보</label>
</span>
	
		<span>
	<label for="licItem5006335"><input type="checkbox" id="licItem5006335" name="licItem" onclick="fnCheckItem('5006335', '가스기능사', 'lic', this)"> 가스기능사</label>
</span>
	
		<span>
	<label for="licItem5003375"><input type="checkbox" id="licItem5003375" name="licItem" onclick="fnCheckItem('5003375', '가스기능장', 'lic', this)"> 가스기능장</label>
</span>
	
		<span>
	<label for="licItem5001471"><input type="checkbox" id="licItem5001471" name="licItem" onclick="fnCheckItem('5001471', '가스기사', 'lic', this)"> 가스기사</label>
</span>
	
		<span>
	<label for="licItem5000752"><input type="checkbox" id="licItem5000752" name="licItem" onclick="fnCheckItem('5000752', '가스기술사', 'lic', this)"> 가스기술사</label>
</span>
	
		<span>
	<label for="licItem5002471"><input type="checkbox" id="licItem5002471" name="licItem" onclick="fnCheckItem('5002471', '가스산업기사', 'lic', this)"> 가스산업기사</label>
</span>
	
		<span>
	<label for="licItem5008190"><input type="checkbox" id="licItem5008190" name="licItem" onclick="fnCheckItem('5008190', '가스용접기능사보', 'lic', this)"> 가스용접기능사보</label>
</span>
	
		<span>
	<label for="licItem5006670"><input type="checkbox" id="licItem5006670" name="licItem" onclick="fnCheckItem('5006670', '가죽처리기능사', 'lic', this)"> 가죽처리기능사</label>
</span>
	
		<span>
	<label for="licItem5008560"><input type="checkbox" id="licItem5008560" name="licItem" onclick="fnCheckItem('5008560', '가죽처리기능사보', 'lic', this)"> 가죽처리기능사보</label>
</span>
	
		<span>
	<label for="licItem5003350"><input type="checkbox" id="licItem5003350" name="licItem" onclick="fnCheckItem('5003350', '가죽처리기능장', 'lic', this)"> 가죽처리기능장</label>
</span>
	
		<span>
	<label for="licItem5004670"><input type="checkbox" id="licItem5004670" name="licItem" onclick="fnCheckItem('5004670', '가죽처리산업기사', 'lic', this)"> 가죽처리산업기사</label>
</span>
	
		<span>
	<label for="licItem5008310"><input type="checkbox" id="licItem5008310" name="licItem" onclick="fnCheckItem('5008310', '객화차정비기능사보', 'lic', this)"> 객화차정비기능사보</label>
</span>
	
		<span>
	<label for="licItem5007050"><input type="checkbox" id="licItem5007050" name="licItem" onclick="fnCheckItem('5007050', '갱부기능사', 'lic', this)"> 갱부기능사</label>
</span>
	
		<span>
	<label for="licItem5008820"><input type="checkbox" id="licItem5008820" name="licItem" onclick="fnCheckItem('5008820', '갱부기능사보', 'lic', this)"> 갱부기능사보</label>
</span>
	
		<span>
	<label for="licItem5003540"><input type="checkbox" id="licItem5003540" name="licItem" onclick="fnCheckItem('5003540', '갱부기능장', 'lic', this)"> 갱부기능장</label>
</span>
	
		<span>
	<label for="licItem5007170"><input type="checkbox" id="licItem5007170" name="licItem" onclick="fnCheckItem('5007170', '거푸집기능사', 'lic', this)"> 거푸집기능사</label>
</span>
	
		<span>
	<label for="licItem5008930"><input type="checkbox" id="licItem5008930" name="licItem" onclick="fnCheckItem('5008930', '거푸집기능사보', 'lic', this)"> 거푸집기능사보</label>
</span>
	
		<span>
	<label for="licItem5008242"><input type="checkbox" id="licItem5008242" name="licItem" onclick="fnCheckItem('5008242', '건설기계기관정비기능사보', 'lic', this)"> 건설기계기관정비기능사보</label>
</span>
	
		<span>
	<label for="licItem5000080"><input type="checkbox" id="licItem5000080" name="licItem" onclick="fnCheckItem('5000080', '건설기계기술사', 'lic', this)"> 건설기계기술사</label>
</span>
	
		<span>
	<label for="licItem5010030"><input type="checkbox" id="licItem5010030" name="licItem" onclick="fnCheckItem('5010030', '건설기계설비기사', 'lic', this)"> 건설기계설비기사</label>
</span>
	
		<span>
	<label for="licItem5010071"><input type="checkbox" id="licItem5010071" name="licItem" onclick="fnCheckItem('5010071', '건설기계설비산업기사', 'lic', this)"> 건설기계설비산업기사</label>
</span>
	
		<span>
	<label for="licItem5006298"><input type="checkbox" id="licItem5006298" name="licItem" onclick="fnCheckItem('5006298', '건설기계정비기능사', 'lic', this)"> 건설기계정비기능사</label>
</span>
	
		<span>
	<label for="licItem5003120"><input type="checkbox" id="licItem5003120" name="licItem" onclick="fnCheckItem('5003120', '건설기계정비기능장', 'lic', this)"> 건설기계정비기능장</label>
</span>
	
		<span>
	<label for="licItem5001050"><input type="checkbox" id="licItem5001050" name="licItem" onclick="fnCheckItem('5001050', '건설기계정비기사', 'lic', this)"> 건설기계정비기사</label>
</span>
	
		<span>
	<label for="licItem5002050"><input type="checkbox" id="licItem5002050" name="licItem" onclick="fnCheckItem('5002050', '건설기계정비산업기사', 'lic', this)"> 건설기계정비산업기사</label>
</span>
	
		<span>
	<label for="licItem5008241"><input type="checkbox" id="licItem5008241" name="licItem" onclick="fnCheckItem('5008241', '건설기계차체정비기능사보', 'lic', this)"> 건설기계차체정비기능사보</label>
</span>
	
		<span>
	<label for="licItem5001440"><input type="checkbox" id="licItem5001440" name="licItem" onclick="fnCheckItem('5001440', '건설안전기사', 'lic', this)"> 건설안전기사</label>
</span>
	
		<span>
	<label for="licItem5000740"><input type="checkbox" id="licItem5000740" name="licItem" onclick="fnCheckItem('5000740', '건설안전기술사', 'lic', this)"> 건설안전기술사</label>
</span>
	
		<span>
	<label for="licItem5002390"><input type="checkbox" id="licItem5002390" name="licItem" onclick="fnCheckItem('5002390', '건설안전산업기사', 'lic', this)"> 건설안전산업기사</label>
</span>
	
		<span>
	<label for="licItem5007132"><input type="checkbox" id="licItem5007132" name="licItem" onclick="fnCheckItem('5007132', '건설재료시험기능사', 'lic', this)"> 건설재료시험기능사</label>
</span>
	
		<span>
	<label for="licItem5001750"><input type="checkbox" id="licItem5001750" name="licItem" onclick="fnCheckItem('5001750', '건설재료시험기사', 'lic', this)"> 건설재료시험기사</label>
</span>
	
		<span>
	<label for="licItem5002600"><input type="checkbox" id="licItem5002600" name="licItem" onclick="fnCheckItem('5002600', '건설재료시험산업기사', 'lic', this)"> 건설재료시험산업기사</label>
</span>
	
		<span>
	<label for="licItem5000490"><input type="checkbox" id="licItem5000490" name="licItem" onclick="fnCheckItem('5000490', '건축구조기술사', 'lic', this)"> 건축구조기술사</label>
</span>
	
		<span>
	<label for="licItem5000501"><input type="checkbox" id="licItem5000501" name="licItem" onclick="fnCheckItem('5000501', '건축기계설비기술사', 'lic', this)"> 건축기계설비기술사</label>
</span>
	
		<span>
	<label for="licItem5001630"><input type="checkbox" id="licItem5001630" name="licItem" onclick="fnCheckItem('5001630', '건축기사', 'lic', this)"> 건축기사</label>
</span>
	
		<span>
	<label for="licItem5007150"><input type="checkbox" id="licItem5007150" name="licItem" onclick="fnCheckItem('5007150', '건축도장기능사', 'lic', this)"> 건축도장기능사</label>
</span>
	
		<span>
	<label for="licItem5008910"><input type="checkbox" id="licItem5008910" name="licItem" onclick="fnCheckItem('5008910', '건축도장기능사보', 'lic', this)"> 건축도장기능사보</label>
</span>
	
		<span>
	<label for="licItem5005090"><input type="checkbox" id="licItem5005090" name="licItem" onclick="fnCheckItem('5005090', '건축도장산업기사', 'lic', this)"> 건축도장산업기사</label>
</span>
	
		<span>
	<label for="licItem5007130"><input type="checkbox" id="licItem5007130" name="licItem" onclick="fnCheckItem('5007130', '건축목공기능사', 'lic', this)"> 건축목공기능사</label>
</span>
	
		<span>
	<label for="licItem5008890"><input type="checkbox" id="licItem5008890" name="licItem" onclick="fnCheckItem('5008890', '건축목공기능사보', 'lic', this)"> 건축목공기능사보</label>
</span>
	
		<span>
	<label for="licItem5002253"><input type="checkbox" id="licItem5002253" name="licItem" onclick="fnCheckItem('5002253', '건축목공산업기사', 'lic', this)"> 건축목공산업기사</label>
</span>
	
		<span>
	<label for="licItem5003611"><input type="checkbox" id="licItem5003611" name="licItem" onclick="fnCheckItem('5003611', '건축목재시공기능장', 'lic', this)"> 건축목재시공기능장</label>
</span>
	
		<span>
	<label for="licItem5008173"><input type="checkbox" id="licItem5008173" name="licItem" onclick="fnCheckItem('5008173', '건축배관기능사보', 'lic', this)"> 건축배관기능사보</label>
</span>
	
		<span>
	<label for="licItem5002530"><input type="checkbox" id="licItem5002530" name="licItem" onclick="fnCheckItem('5002530', '건축산업기사', 'lic', this)"> 건축산업기사</label>
</span>
	
		<span>
	<label for="licItem5001632"><input type="checkbox" id="licItem5001632" name="licItem" onclick="fnCheckItem('5001632', '건축설비기사', 'lic', this)"> 건축설비기사</label>
</span>
	
		<span>
	<label for="licItem5002531"><input type="checkbox" id="licItem5002531" name="licItem" onclick="fnCheckItem('5002531', '건축설비산업기사', 'lic', this)"> 건축설비산업기사</label>
</span>
	
		<span>
	<label for="licItem5000510"><input type="checkbox" id="licItem5000510" name="licItem" onclick="fnCheckItem('5000510', '건축시공기술사', 'lic', this)"> 건축시공기술사</label>
</span>
	
		<span>
	<label for="licItem5003621"><input type="checkbox" id="licItem5003621" name="licItem" onclick="fnCheckItem('5003621', '건축일반시공기능장', 'lic', this)"> 건축일반시공기능장</label>
</span>
	
		<span>
	<label for="licItem5002251"><input type="checkbox" id="licItem5002251" name="licItem" onclick="fnCheckItem('5002251', '건축일반시공산업기사', 'lic', this)"> 건축일반시공산업기사</label>
</span>
	
		<span>
	<label for="licItem5008131"><input type="checkbox" id="licItem5008131" name="licItem" onclick="fnCheckItem('5008131', '건축재료시험기능사보', 'lic', this)"> 건축재료시험기능사보</label>
</span>
	
		<span>
	<label for="licItem5000502"><input type="checkbox" id="licItem5000502" name="licItem" onclick="fnCheckItem('5000502', '건축전기설비기술사', 'lic', this)"> 건축전기설비기술사</label>
</span>
	
		<span>
	<label for="licItem5003550"><input type="checkbox" id="licItem5003550" name="licItem" onclick="fnCheckItem('5003550', '건축제도기능장', 'lic', this)"> 건축제도기능장</label>
</span>
	
		<span>
	<label for="licItem5005000"><input type="checkbox" id="licItem5005000" name="licItem" onclick="fnCheckItem('5005000', '건축제도산업기사', 'lic', this)"> 건축제도산업기사</label>
</span>
	
		<span>
	<label for="licItem5000511"><input type="checkbox" id="licItem5000511" name="licItem" onclick="fnCheckItem('5000511', '건축품질시험기술사', 'lic', this)"> 건축품질시험기술사</label>
</span>
	
		<span>
	<label for="licItem5009543"><input type="checkbox" id="licItem5009543" name="licItem" onclick="fnCheckItem('5009543', '게임그래픽전문가', 'lic', this)"> 게임그래픽전문가</label>
</span>
	
		<span>
	<label for="licItem5009544"><input type="checkbox" id="licItem5009544" name="licItem" onclick="fnCheckItem('5009544', '게임기획전문가', 'lic', this)"> 게임기획전문가</label>
</span>
	
		<span>
	<label for="licItem5009542"><input type="checkbox" id="licItem5009542" name="licItem" onclick="fnCheckItem('5009542', '게임프로그래밍전문가', 'lic', this)"> 게임프로그래밍전문가</label>
</span>
	
		<span>
	<label for="licItem5001713"><input type="checkbox" id="licItem5001713" name="licItem" onclick="fnCheckItem('5001713', '계량기사(기계분야)', 'lic', this)"> 계량기사(기계분야)</label>
</span>
	
		<span>
	<label for="licItem5001720"><input type="checkbox" id="licItem5001720" name="licItem" onclick="fnCheckItem('5001720', '계량기사(물리분야)', 'lic', this)"> 계량기사(물리분야)</label>
</span>
	
		<span>
	<label for="licItem5001703"><input type="checkbox" id="licItem5001703" name="licItem" onclick="fnCheckItem('5001703', '계량기사(전기분야)	', 'lic', this)"> 계량기사(전기분야)	</label>
</span>
	
		<span>
	<label for="licItem5006640"><input type="checkbox" id="licItem5006640" name="licItem" onclick="fnCheckItem('5006640', '고무제품제조기능사', 'lic', this)"> 고무제품제조기능사</label>
</span>
	
		<span>
	<label for="licItem5008530"><input type="checkbox" id="licItem5008530" name="licItem" onclick="fnCheckItem('5008530', '고무제품제조기능사보', 'lic', this)"> 고무제품제조기능사보</label>
</span>
	
		<span>
	<label for="licItem5003320"><input type="checkbox" id="licItem5003320" name="licItem" onclick="fnCheckItem('5003320', '고무제품제조기능장', 'lic', this)"> 고무제품제조기능장</label>
</span>
	
		<span>
	<label for="licItem5004640"><input type="checkbox" id="licItem5004640" name="licItem" onclick="fnCheckItem('5004640', '고무제품제조산업기사', 'lic', this)"> 고무제품제조산업기사</label>
</span>
	
		<span>
	<label for="licItem5006642"><input type="checkbox" id="licItem5006642" name="licItem" onclick="fnCheckItem('5006642', '고분자제품제조기능사', 'lic', this)"> 고분자제품제조기능사</label>
</span>
	
		<span>
	<label for="licItem5008260"><input type="checkbox" id="licItem5008260" name="licItem" onclick="fnCheckItem('5008260', '고압가스기계기능사보', 'lic', this)"> 고압가스기계기능사보</label>
</span>
	
		<span>
	<label for="licItem5008270"><input type="checkbox" id="licItem5008270" name="licItem" onclick="fnCheckItem('5008270', '고압가스냉동기계기능사보', 'lic', this)"> 고압가스냉동기계기능사보</label>
</span>
	
		<span>
	<label for="licItem5008280"><input type="checkbox" id="licItem5008280" name="licItem" onclick="fnCheckItem('5008280', '고압가스취급기능사보', 'lic', this)"> 고압가스취급기능사보</label>
</span>
	
		<span>
	<label for="licItem5008570"><input type="checkbox" id="licItem5008570" name="licItem" onclick="fnCheckItem('5008570', '고압가스화학기능사보', 'lic', this)"> 고압가스화학기능사보</label>
</span>
	
		<span>
	<label for="licItem5007882"><input type="checkbox" id="licItem5007882" name="licItem" onclick="fnCheckItem('5007882', '고압합성기능사', 'lic', this)"> 고압합성기능사</label>
</span>
	
		<span>
	<label for="licItem5009432"><input type="checkbox" id="licItem5009432" name="licItem" onclick="fnCheckItem('5009432', '고압합성기능사보', 'lic', this)"> 고압합성기능사보</label>
</span>
	
		<span>
	<label for="licItem5006090"><input type="checkbox" id="licItem5006090" name="licItem" onclick="fnCheckItem('5006090', '공구제작기능사', 'lic', this)"> 공구제작기능사</label>
</span>
	
		<span>
	<label for="licItem5008070"><input type="checkbox" id="licItem5008070" name="licItem" onclick="fnCheckItem('5008070', '공구제작기능사보', 'lic', this)"> 공구제작기능사보</label>
</span>
	
		<span>
	<label for="licItem5005764"><input type="checkbox" id="licItem5005764" name="licItem" onclick="fnCheckItem('5005764', '공기압축기산업기사', 'lic', this)"> 공기압축기산업기사</label>
</span>
	
		<span>
	<label for="licItem5007876"><input type="checkbox" id="licItem5007876" name="licItem" onclick="fnCheckItem('5007876', '공기압축기운전기능사', 'lic', this)"> 공기압축기운전기능사</label>
</span>
	
		<span>
	<label for="licItem5006380"><input type="checkbox" id="licItem5006380" name="licItem" onclick="fnCheckItem('5006380', '공기조화기능사', 'lic', this)"> 공기조화기능사</label>
</span>
	
		<span>
	<label for="licItem5008320"><input type="checkbox" id="licItem5008320" name="licItem" onclick="fnCheckItem('5008320', '공기조화기능사보', 'lic', this)"> 공기조화기능사보</label>
</span>
	
		<span>
	<label for="licItem5003160"><input type="checkbox" id="licItem5003160" name="licItem" onclick="fnCheckItem('5003160', '공기조화기능장', 'lic', this)"> 공기조화기능장</label>
</span>
	
		<span>
	<label for="licItem5007790"><input type="checkbox" id="licItem5007790" name="licItem" onclick="fnCheckItem('5007790', '공업계측제어기능사', 'lic', this)"> 공업계측제어기능사</label>
</span>
	
		<span>
	<label for="licItem5001640"><input type="checkbox" id="licItem5001640" name="licItem" onclick="fnCheckItem('5001640', '공업계측제어기사', 'lic', this)"> 공업계측제어기사</label>
</span>
	
		<span>
	<label for="licItem5005700"><input type="checkbox" id="licItem5005700" name="licItem" onclick="fnCheckItem('5005700', '공업계측제어산업기사', 'lic', this)"> 공업계측제어산업기사</label>
</span>
	
		<span>
	<label for="licItem5008174"><input type="checkbox" id="licItem5008174" name="licItem" onclick="fnCheckItem('5008174', '공업배관기능사보', 'lic', this)"> 공업배관기능사보</label>
</span>
	
		<span>
	<label for="licItem5006251"><input type="checkbox" id="licItem5006251" name="licItem" onclick="fnCheckItem('5006251', '공유압기능사', 'lic', this)"> 공유압기능사</label>
</span>
	
		<span>
	<label for="licItem5000760"><input type="checkbox" id="licItem5000760" name="licItem" onclick="fnCheckItem('5000760', '공장관리기술사', 'lic', this)"> 공장관리기술사</label>
</span>
	
		<span>
	<label for="licItem5002080"><input type="checkbox" id="licItem5002080" name="licItem" onclick="fnCheckItem('5002080', '공정설계산업기사', 'lic', this)"> 공정설계산업기사</label>
</span>
	
		<span>
	<label for="licItem5006320"><input type="checkbox" id="licItem5006320" name="licItem" onclick="fnCheckItem('5006320', '공조냉동기계기능사', 'lic', this)"> 공조냉동기계기능사</label>
</span>
	
		<span>
	<label for="licItem5001730"><input type="checkbox" id="licItem5001730" name="licItem" onclick="fnCheckItem('5001730', '공조냉동기계기사', 'lic', this)"> 공조냉동기계기사</label>
</span>
	
		<span>
	<label for="licItem5000071"><input type="checkbox" id="licItem5000071" name="licItem" onclick="fnCheckItem('5000071', '공조냉동기계기술사', 'lic', this)"> 공조냉동기계기술사</label>
</span>
	
		<span>
	<label for="licItem5002590"><input type="checkbox" id="licItem5002590" name="licItem" onclick="fnCheckItem('5002590', '공조냉동기계산업기사', 'lic', this)"> 공조냉동기계산업기사</label>
</span>
	
		<span>
	<label for="licItem5009448"><input type="checkbox" id="licItem5009448" name="licItem" onclick="fnCheckItem('5009448', '과수재배기능사보', 'lic', this)"> 과수재배기능사보</label>
</span>
	
		<span>
	<label for="licItem5007888"><input type="checkbox" id="licItem5007888" name="licItem" onclick="fnCheckItem('5007888', '광고도장기능사', 'lic', this)"> 광고도장기능사</label>
</span>
	
		<span>
	<label for="licItem5009435"><input type="checkbox" id="licItem5009435" name="licItem" onclick="fnCheckItem('5009435', '광고도장기능사보', 'lic', this)"> 광고도장기능사보</label>
</span>
	
		<span>
	<label for="licItem5005777"><input type="checkbox" id="licItem5005777" name="licItem" onclick="fnCheckItem('5005777', '광고도장산업기사', 'lic', this)"> 광고도장산업기사</label>
</span>
	
		<span>
	<label for="licItem5007361"><input type="checkbox" id="licItem5007361" name="licItem" onclick="fnCheckItem('5007361', '광산기계기능사', 'lic', this)"> 광산기계기능사</label>
</span>
	
		<span>
	<label for="licItem5008361"><input type="checkbox" id="licItem5008361" name="licItem" onclick="fnCheckItem('5008361', '광산기계기능사보', 'lic', this)"> 광산기계기능사보</label>
</span>
	
		<span>
	<label for="licItem5007360"><input type="checkbox" id="licItem5007360" name="licItem" onclick="fnCheckItem('5007360', '광산기계설치기능사', 'lic', this)"> 광산기계설치기능사</label>
</span>
	
		<span>
	<label for="licItem5009120"><input type="checkbox" id="licItem5009120" name="licItem" onclick="fnCheckItem('5009120', '광산기계설치기능사보', 'lic', this)"> 광산기계설치기능사보</label>
</span>
	
		<span>
	<label for="licItem5007370"><input type="checkbox" id="licItem5007370" name="licItem" onclick="fnCheckItem('5007370', '광산기계운전및수리기능사', 'lic', this)"> 광산기계운전및수리기능사</label>
</span>
	
		<span>
	<label for="licItem5003710"><input type="checkbox" id="licItem5003710" name="licItem" onclick="fnCheckItem('5003710', '광산기계운전및수리기능장', 'lic', this)"> 광산기계운전및수리기능장</label>
</span>
	
		<span>
	<label for="licItem5010149"><input type="checkbox" id="licItem5010149" name="licItem" onclick="fnCheckItem('5010149', '광산보안기능사', 'lic', this)"> 광산보안기능사</label>
</span>
	
		<span>
	<label for="licItem5001450"><input type="checkbox" id="licItem5001450" name="licItem" onclick="fnCheckItem('5001450', '광산보안기사', 'lic', this)"> 광산보안기사</label>
</span>
	
		<span>
	<label for="licItem5002135"><input type="checkbox" id="licItem5002135" name="licItem" onclick="fnCheckItem('5002135', '광산보안산업기사', 'lic', this)"> 광산보안산업기사</label>
</span>
	
		<span>
	<label for="licItem5002108"><input type="checkbox" id="licItem5002108" name="licItem" onclick="fnCheckItem('5002108', '광학기기산업기사', 'lic', this)"> 광학기기산업기사</label>
</span>
	
		<span>
	<label for="licItem5007671"><input type="checkbox" id="licItem5007671" name="licItem" onclick="fnCheckItem('5007671', '광학기능사', 'lic', this)"> 광학기능사</label>
</span>
	
		<span>
	<label for="licItem5001513"><input type="checkbox" id="licItem5001513" name="licItem" onclick="fnCheckItem('5001513', '광학기사', 'lic', this)"> 광학기사</label>
</span>
	
		<span>
	<label for="licItem5002433"><input type="checkbox" id="licItem5002433" name="licItem" onclick="fnCheckItem('5002433', '광학산업기사', 'lic', this)"> 광학산업기사</label>
</span>
	
		<span>
	<label for="licItem5001575"><input type="checkbox" id="licItem5001575" name="licItem" onclick="fnCheckItem('5001575', '광해방지기사', 'lic', this)"> 광해방지기사</label>
</span>
	
		<span>
	<label for="licItem5000575"><input type="checkbox" id="licItem5000575" name="licItem" onclick="fnCheckItem('5000575', '광해방지기술사', 'lic', this)"> 광해방지기술사</label>
</span>
	
		<span>
	<label for="licItem5001751"><input type="checkbox" id="licItem5001751" name="licItem" onclick="fnCheckItem('5001751', '교통기사', 'lic', this)"> 교통기사</label>
</span>
	
		<span>
	<label for="licItem5000951"><input type="checkbox" id="licItem5000951" name="licItem" onclick="fnCheckItem('5000951', '교통기술사', 'lic', this)"> 교통기술사</label>
</span>
	
		<span>
	<label for="licItem5002751"><input type="checkbox" id="licItem5002751" name="licItem" onclick="fnCheckItem('5002751', '교통산업기사', 'lic', this)"> 교통산업기사</label>
</span>
	
		<span>
	<label for="licItem5009371"><input type="checkbox" id="licItem5009371" name="licItem" onclick="fnCheckItem('5009371', '교환설비기능사보', 'lic', this)"> 교환설비기능사보</label>
</span>
	
		<span>
	<label for="licItem5008921"><input type="checkbox" id="licItem5008921" name="licItem" onclick="fnCheckItem('5008921', '구들온돌기능사보', 'lic', this)"> 구들온돌기능사보</label>
</span>
	
		<span>
	<label for="licItem5010012"><input type="checkbox" id="licItem5010012" name="licItem" onclick="fnCheckItem('5010012', '국제의료관광코디네이터', 'lic', this)"> 국제의료관광코디네이터</label>
</span>
	
		<span>
	<label for="licItem5009090"><input type="checkbox" id="licItem5009090" name="licItem" onclick="fnCheckItem('5009090', '굴진기능사보', 'lic', this)"> 굴진기능사보</label>
</span>
	
		<span>
	<label for="licItem5009080"><input type="checkbox" id="licItem5009080" name="licItem" onclick="fnCheckItem('5009080', '굴착기능사보', 'lic', this)"> 굴착기능사보</label>
</span>
	
		<span>
	<label for="licItem5007862"><input type="checkbox" id="licItem5007862" name="licItem" onclick="fnCheckItem('5007862', '굴착기운전기능사', 'lic', this)"> 굴착기운전기능사</label>
</span>
	
		<span>
	<label for="licItem5002279"><input type="checkbox" id="licItem5002279" name="licItem" onclick="fnCheckItem('5002279', '굴착산업기사', 'lic', this)"> 굴착산업기사</label>
</span>
	
		<span>
	<label for="licItem5007692"><input type="checkbox" id="licItem5007692" name="licItem" onclick="fnCheckItem('5007692', '궐련제조기계정비기능사', 'lic', this)"> 궐련제조기계정비기능사</label>
</span>
	
		<span>
	<label for="licItem5006412"><input type="checkbox" id="licItem5006412" name="licItem" onclick="fnCheckItem('5006412', '궐련제조기능사', 'lic', this)"> 궐련제조기능사</label>
</span>
	
		<span>
	<label for="licItem5008332"><input type="checkbox" id="licItem5008332" name="licItem" onclick="fnCheckItem('5008332', '궐련제조기능사보', 'lic', this)"> 궐련제조기능사보</label>
</span>
	
		<span>
	<label for="licItem5006051"><input type="checkbox" id="licItem5006051" name="licItem" onclick="fnCheckItem('5006051', '궤도장비정비기능사', 'lic', this)"> 궤도장비정비기능사</label>
</span>
	
		<span>
	<label for="licItem5001051"><input type="checkbox" id="licItem5001051" name="licItem" onclick="fnCheckItem('5001051', '궤도장비정비기사', 'lic', this)"> 궤도장비정비기사</label>
</span>
	
		<span>
	<label for="licItem5002051"><input type="checkbox" id="licItem5002051" name="licItem" onclick="fnCheckItem('5002051', '궤도장비정비산업기사', 'lic', this)"> 궤도장비정비산업기사</label>
</span>
	
		<span>
	<label for="licItem5007460"><input type="checkbox" id="licItem5007460" name="licItem" onclick="fnCheckItem('5007460', '귀금속가공기능사', 'lic', this)"> 귀금속가공기능사</label>
</span>
	
		<span>
	<label for="licItem5009200"><input type="checkbox" id="licItem5009200" name="licItem" onclick="fnCheckItem('5009200', '귀금속가공기능사보', 'lic', this)"> 귀금속가공기능사보</label>
</span>
	
		<span>
	<label for="licItem5003770"><input type="checkbox" id="licItem5003770" name="licItem" onclick="fnCheckItem('5003770', '귀금속가공기능장', 'lic', this)"> 귀금속가공기능장</label>
</span>
	
		<span>
	<label for="licItem5002760"><input type="checkbox" id="licItem5002760" name="licItem" onclick="fnCheckItem('5002760', '귀금속가공산업기사', 'lic', this)"> 귀금속가공산업기사</label>
</span>
	
		<span>
	<label for="licItem5009480"><input type="checkbox" id="licItem5009480" name="licItem" onclick="fnCheckItem('5009480', '그라비아인쇄기능사보', 'lic', this)"> 그라비아인쇄기능사보</label>
</span>
	
		<span>
	<label for="licItem5000041"><input type="checkbox" id="licItem5000041" name="licItem" onclick="fnCheckItem('5000041', '그린전동자동차기사', 'lic', this)"> 그린전동자동차기사</label>
</span>
	
		<span>
	<label for="licItem5000130"><input type="checkbox" id="licItem5000130" name="licItem" onclick="fnCheckItem('5000130', '금속가공기술사', 'lic', this)"> 금속가공기술사</label>
</span>
	
		<span>
	<label for="licItem5007440"><input type="checkbox" id="licItem5007440" name="licItem" onclick="fnCheckItem('5007440', '금속공예기능사', 'lic', this)"> 금속공예기능사</label>
</span>
	
		<span>
	<label for="licItem5009180"><input type="checkbox" id="licItem5009180" name="licItem" onclick="fnCheckItem('5009180', '금속공예기능사보', 'lic', this)"> 금속공예기능사보</label>
</span>
	
		<span>
	<label for="licItem5003750"><input type="checkbox" id="licItem5003750" name="licItem" onclick="fnCheckItem('5003750', '금속공예기능장', 'lic', this)"> 금속공예기능장</label>
</span>
	
		<span>
	<label for="licItem5006009"><input type="checkbox" id="licItem5006009" name="licItem" onclick="fnCheckItem('5006009', '금속기사(제련분야)', 'lic', this)"> 금속기사(제련분야)</label>
</span>
	
		<span>
	<label for="licItem5007450"><input type="checkbox" id="licItem5007450" name="licItem" onclick="fnCheckItem('5007450', '금속도장기능사', 'lic', this)"> 금속도장기능사</label>
</span>
	
		<span>
	<label for="licItem5009190"><input type="checkbox" id="licItem5009190" name="licItem" onclick="fnCheckItem('5009190', '금속도장기능사보', 'lic', this)"> 금속도장기능사보</label>
</span>
	
		<span>
	<label for="licItem5003760"><input type="checkbox" id="licItem5003760" name="licItem" onclick="fnCheckItem('5003760', '금속도장기능장', 'lic', this)"> 금속도장기능장</label>
</span>
	
		<span>
	<label for="licItem5005380"><input type="checkbox" id="licItem5005380" name="licItem" onclick="fnCheckItem('5005380', '금속도장산업기사', 'lic', this)"> 금속도장산업기사</label>
</span>
	
		<span>
	<label for="licItem5003221"><input type="checkbox" id="licItem5003221" name="licItem" onclick="fnCheckItem('5003221', '금속재료기능장', 'lic', this)"> 금속재료기능장</label>
</span>
	
		<span>
	<label for="licItem5010032"><input type="checkbox" id="licItem5010032" name="licItem" onclick="fnCheckItem('5010032', '금속재료기사', 'lic', this)"> 금속재료기사</label>
</span>
	
		<span>
	<label for="licItem5000110"><input type="checkbox" id="licItem5000110" name="licItem" onclick="fnCheckItem('5000110', '금속재료기술사', 'lic', this)"> 금속재료기술사</label>
</span>
	
		<span>
	<label for="licItem5002101"><input type="checkbox" id="licItem5002101" name="licItem" onclick="fnCheckItem('5002101', '금속재료산업기사', 'lic', this)"> 금속재료산업기사</label>
</span>
	
		<span>
	<label for="licItem5006490"><input type="checkbox" id="licItem5006490" name="licItem" onclick="fnCheckItem('5006490', '금속재료시험기능사', 'lic', this)"> 금속재료시험기능사</label>
</span>
	
		<span>
	<label for="licItem5007102"><input type="checkbox" id="licItem5007102" name="licItem" onclick="fnCheckItem('5007102', '금속재창호기능사', 'lic', this)"> 금속재창호기능사</label>
</span>
	
		<span>
	<label for="licItem5008862"><input type="checkbox" id="licItem5008862" name="licItem" onclick="fnCheckItem('5008862', '금속재창호기능사보', 'lic', this)"> 금속재창호기능사보</label>
</span>
	
		<span>
	<label for="licItem5000094"><input type="checkbox" id="licItem5000094" name="licItem" onclick="fnCheckItem('5000094', '금속제련기술사', 'lic', this)"> 금속제련기술사</label>
</span>
	
		<span>
	<label for="licItem5002102"><input type="checkbox" id="licItem5002102" name="licItem" onclick="fnCheckItem('5002102', '금속제련산업기사', 'lic', this)"> 금속제련산업기사</label>
</span>
	
		<span>
	<label for="licItem5006105"><input type="checkbox" id="licItem5006105" name="licItem" onclick="fnCheckItem('5006105', '금형기능사', 'lic', this)"> 금형기능사</label>
</span>
	
		<span>
	<label for="licItem5000012"><input type="checkbox" id="licItem5000012" name="licItem" onclick="fnCheckItem('5000012', '금형기술사', 'lic', this)"> 금형기술사</label>
</span>
	
		<span>
	<label for="licItem5003061"><input type="checkbox" id="licItem5003061" name="licItem" onclick="fnCheckItem('5003061', '금형제작기능장', 'lic', this)"> 금형제작기능장</label>
</span>
	
		<span>
	<label for="licItem5003021"><input type="checkbox" id="licItem5003021" name="licItem" onclick="fnCheckItem('5003021', '기계가공기능장', 'lic', this)"> 기계가공기능장</label>
</span>
	
		<span>
	<label for="licItem5010010"><input type="checkbox" id="licItem5010010" name="licItem" onclick="fnCheckItem('5010010', '기계가공조립기능사', 'lic', this)"> 기계가공조립기능사</label>
</span>
	
		<span>
	<label for="licItem5003030"><input type="checkbox" id="licItem5003030" name="licItem" onclick="fnCheckItem('5003030', '기계검사및설치기능장', 'lic', this)"> 기계검사및설치기능장</label>
</span>
	
		<span>
	<label for="licItem5000872"><input type="checkbox" id="licItem5000872" name="licItem" onclick="fnCheckItem('5000872', '기계기술사', 'lic', this)"> 기계기술사</label>
</span>
	
		<span>
	<label for="licItem5000871"><input type="checkbox" id="licItem5000871" name="licItem" onclick="fnCheckItem('5000871', '기계기술사(정밀측정)', 'lic', this)"> 기계기술사(정밀측정)</label>
</span>
	
		<span>
	<label for="licItem5002031"><input type="checkbox" id="licItem5002031" name="licItem" onclick="fnCheckItem('5002031', '기계설계산업기사', 'lic', this)"> 기계설계산업기사</label>
</span>
	
		<span>
	<label for="licItem5000710"><input type="checkbox" id="licItem5000710" name="licItem" onclick="fnCheckItem('5000710', '기계안전기술사', 'lic', this)"> 기계안전기술사</label>
</span>
	
		<span>
	<label for="licItem5009402"><input type="checkbox" id="licItem5009402" name="licItem" onclick="fnCheckItem('5009402', '기계자수공예기능사보', 'lic', this)"> 기계자수공예기능사보</label>
</span>
	
		<span>
	<label for="licItem5003070"><input type="checkbox" id="licItem5003070" name="licItem" onclick="fnCheckItem('5003070', '기계제도기능장', 'lic', this)"> 기계제도기능장</label>
</span>
	
		<span>
	<label for="licItem5004150"><input type="checkbox" id="licItem5004150" name="licItem" onclick="fnCheckItem('5004150', '기계제도산업기사', 'lic', this)"> 기계제도산업기사</label>
</span>
	
		<span>
	<label for="licItem5010011"><input type="checkbox" id="licItem5010011" name="licItem" onclick="fnCheckItem('5010011', '기계조립산업기사', 'lic', this)"> 기계조립산업기사</label>
</span>
	
		<span>
	<label for="licItem5009392"><input type="checkbox" id="licItem5009392" name="licItem" onclick="fnCheckItem('5009392', '기계편물기능사보', 'lic', this)"> 기계편물기능사보</label>
</span>
	
		<span>
	<label for="licItem5001601"><input type="checkbox" id="licItem5001601" name="licItem" onclick="fnCheckItem('5001601', '기상감정기사', 'lic', this)"> 기상감정기사</label>
</span>
	
		<span>
	<label for="licItem5001600"><input type="checkbox" id="licItem5001600" name="licItem" onclick="fnCheckItem('5001600', '기상기사', 'lic', this)"> 기상기사</label>
</span>
	
		<span>
	<label for="licItem5002510"><input type="checkbox" id="licItem5002510" name="licItem" onclick="fnCheckItem('5002510', '기상산업기사', 'lic', this)"> 기상산업기사</label>
</span>
	
		<span>
	<label for="licItem5000891"><input type="checkbox" id="licItem5000891" name="licItem" onclick="fnCheckItem('5000891', '기상예보기술사', 'lic', this)"> 기상예보기술사</label>
</span>
	
		<span>
	<label for="licItem5006070"><input type="checkbox" id="licItem5006070" name="licItem" onclick="fnCheckItem('5006070', '기어절삭기능사', 'lic', this)"> 기어절삭기능사</label>
</span>
	
		<span>
	<label for="licItem5008061"><input type="checkbox" id="licItem5008061" name="licItem" onclick="fnCheckItem('5008061', '기어절삭기능사보', 'lic', this)"> 기어절삭기능사보</label>
</span>
	
		<span>
	<label for="licItem5004070"><input type="checkbox" id="licItem5004070" name="licItem" onclick="fnCheckItem('5004070', '기어절삭산업기사', 'lic', this)"> 기어절삭산업기사</label>
</span>
	
		<span>
	<label for="licItem5007190"><input type="checkbox" id="licItem5007190" name="licItem" onclick="fnCheckItem('5007190', '기와기능사', 'lic', this)"> 기와기능사</label>
</span>
	
		<span>
	<label for="licItem5008950"><input type="checkbox" id="licItem5008950" name="licItem" onclick="fnCheckItem('5008950', '기와기능사보', 'lic', this)"> 기와기능사보</label>
</span>
	
		<span>
	<label for="licItem5007861"><input type="checkbox" id="licItem5007861" name="licItem" onclick="fnCheckItem('5007861', '기중기운전기능사', 'lic', this)"> 기중기운전기능사</label>
</span>
	</div>
												</div>
											</div>

											<ul class="box_list_area mt16">
												<li class="txt_list">"[미관리]"로 표기된 자격은 고용24에서는 관리되지 않거나 실제 폐지된 자격을 의미합니다.</li>
												<li class="txt_list">"[미관리]"로 표시된 자격을 입력하시고자 하는 경우, 기타자격 항목에 작성하여 주시기 바랍니다.</li>
											</ul>
										</div>

										<div id="tab-panel-02" class="box_tab-contents" role="tabpanel">
											<div class="list_chk_area only_cont">
												<div class="cont_area mt16">
													<div class="box_chk-group flex_al col_3" id="lic_6">

													</div>
												</div>
											</div>

											<ul class="box_list_area mt16">
												<li class="txt_list">"[미관리]"로 표기된 자격은 고용24에서는 관리되지 않거나 실제 폐지된 자격을 의미합니다.</li>
												<li class="txt_list">"[미관리]"로 표시된 자격을 입력하시고자 하는 경우, 기타자격 항목에 작성하여 주시기 바랍니다.</li>
											</ul>
										</div>

										<div id="tab-panel-03" class="box_tab-contents" role="tabpanel">
											<div class="list_chk_area only_cont">
												<div class="cont_area mt16">
													<div class="box_chk-group flex_al col_3" id="lic_7">

													</div>
												</div>
											</div>

											<ul class="box_list_area mt16">
												<li class="txt_list">"[미관리]"로 표기된 자격은 고용24에서는 관리되지 않거나 실제 폐지된 자격을 의미합니다.</li>
												<li class="txt_list">"[미관리]"로 표시된 자격을 입력하시고자 하는 경우, 기타자격 항목에 작성하여 주시기 바랍니다.</li>
											</ul>
										</div>


									</div>
								</div>

								<div style="display:none;" id="licSearchList">
									<div class="list_chk_area only_cont">
										<div class="cont_area">
											<div class="box_chk-group flex_al col_3" id="licUl">

											</div>
										</div>
									</div>

									<div class="b1_r mt16">
										분류 리스트로 검색하려면 [분류별 보기]버튼을 클릭하세요
										<a href="#none" class="btn medium type02 ml08 " onclick="fn_LicSearch('cate');">분류별 보기</a>
									</div>
								</div>

								<!-- 버튼 -->
								<a href="#none" class="closed" onclick="fn_show('jobLicense');">
									<span class="blind">팝업 닫기</span>
								</a>
								<!--// 버튼 -->
							</div>
							<!--// 본문 컨텐츠 -->

						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">전공</span>
					<div class="cont">
						<button type="button" class="btn medium type02" onclick="fn_show('jobMajor');"><span>전공 선택</span></button>
						<div id="jobMajor" style="display:none " class="layer_section">
							<!-- 본문 컨텐츠 -->
							<!-- 250416 article 태그 삭제 -->
							<table class="search_table mt16"><caption>
										을(를) 제공하는 표</caption>
								
								<colgroup>
									<col style="width:20%;">
									<col>
								</colgroup>
								<tbody>
								<tr>
									<th scope="row">
										<span>검색키워드</span>
									</th>
									<td>
										<div class="box_sch_group">
												<span class="box_ipt">
													<input type="text" id="majorSearchTxt" name="majorSearchTxt" onkeypress="if(event.keyCode==13) fn_MajorSearch('list');" class="input_txt" title="전공 관련 키워드를 입력하세요. 예) 법학, 철학" placeholder="전공 관련 키워드를 입력하세요. 예) 법학, 철학">
													<button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>

												</span>
											<button type="button" class="btn medium fill type01" onclick="fn_MajorSearch('list');">검색</button>
										</div>
									</td>
								</tr>
								</tbody>
							</table>


							<div class="list_chk_area type_col chk_col_type" id="majorCategoryList">
								<div class="col">
									<p class="tit">1차 계열</p>
									<div class="cont_area scroll h280">
										<div class="select_button_list" id="majorUl1">
											
												<button type="button" onclick="fn_GetMajor('2', '01');" id="majorBtn_01">인문계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '02');" id="majorBtn_02">사회계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '03');" id="majorBtn_03">교육계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '04');" id="majorBtn_04">공학계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '05');" id="majorBtn_05">자연계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '06');" id="majorBtn_06">의약계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '07');" id="majorBtn_07">예체능계열</button>
											
												<button type="button" onclick="fn_GetMajor('2', '08');" id="majorBtn_08">자율전공(무전공)</button>
											
										</div>
									</div>
								</div>
								<div class="col">
									<p class="tit">2차 계열</p>
									<div class="cont_area scroll h280">
										<div class="select_button_list" id="majorUl2">
											<button type="button" class="chk">1차 계열을 선택하세요</button>
										</div>
									</div>
								</div>
								<div class="col">
									<p class="tit">3차 계열</p>
									<div class="cont_area scroll h280">
										<div class="select_button_list">
											<ul class="box_chk-group chk_row wd100per" id="majorUl3">
												<button type="button" class="chk">2차 계열을 선택하세요</button>
											</ul>
										</div>
									</div>
								</div>
							</div>
							<div style="display:none;" id="majorSearchList">
								<div class="list_chk_area only_cont">
									<div class="cont_area">
										<p class="b1_r">
											검색결과 (<span class="point_color02" id="majorCnt">0</span>건)
										</p>

										<ul class="box_list_area mt08" id="majorUl">
											<li class="txt_list">
												공학계열 &gt; 교통 · 운송 &gt; 지상교통공학 &gt;
												<div class="box_radio-group">
			                                        <span>
			                                            <input type="radio" name="rdo" id="rdo">
			                                            <label for="rdo">철도전기시스템학과</label>
			                                        </span>
												</div>
											</li>

										</ul>
									</div>
								</div>

								<div class="b1_r mt16">
									분류 리스트로 검색하려면 [분류별 보기]버튼을 클릭하세요
									<a href="#none" class="btn medium type02 ml08 " onclick="fn_MajorSearch('cate');">분류별 보기</a>
								</div>
							</div>
							<!-- 버튼 -->
							<a href="#none" class="closed" onclick="fn_show('jobMajor');">
								<span class="blind">팝업 닫기</span>
							</a>
							<!--// 버튼 -->
							<!--// 본문 컨텐츠 -->
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">외국어</span>
					<div class="cont">
						<button type="button" class="btn medium type02" onclick="fn_show('jobForeignLang');"><span>외국어 선택</span></button>
						<div id="jobForeignLang" style="display:none " class="layer_section">
							<div class="careers-foreign-lang on-scroll mt16">
								<div class="box_chk-group flex_al col_3 view-col-3">
									
										<span>
											<input type="checkbox" name="forItem" id="forItem01" title="영어" value="01" onclick="fnCheckItem('01', '영어', 'for', this)">
											<label for="forItem01">영어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem02" title="일어" value="02" onclick="fnCheckItem('02', '일어', 'for', this)">
											<label for="forItem02">일어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem07" title="중국어" value="07" onclick="fnCheckItem('07', '중국어', 'for', this)">
											<label for="forItem07">중국어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem09" title="아랍어" value="09" onclick="fnCheckItem('09', '아랍어', 'for', this)">
											<label for="forItem09">아랍어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem05" title="서반어" value="05" onclick="fnCheckItem('05', '서반어', 'for', this)">
											<label for="forItem05">서반어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem40" title="인도네시아어" value="40" onclick="fnCheckItem('40', '인도네시아어', 'for', this)">
											<label for="forItem40">인도네시아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem39" title="말레이어" value="39" onclick="fnCheckItem('39', '말레이어', 'for', this)">
											<label for="forItem39">말레이어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem10" title="베트남어" value="10" onclick="fnCheckItem('10', '베트남어', 'for', this)">
											<label for="forItem10">베트남어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem16" title="타이어" value="16" onclick="fnCheckItem('16', '타이어', 'for', this)">
											<label for="forItem16">타이어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem03" title="독일어" value="03" onclick="fnCheckItem('03', '독일어', 'for', this)">
											<label for="forItem03">독일어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem04" title="불어" value="04" onclick="fnCheckItem('04', '불어', 'for', this)">
											<label for="forItem04">불어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem08" title="러시아어" value="08" onclick="fnCheckItem('08', '러시아어', 'for', this)">
											<label for="forItem08">러시아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem11" title="이태리어" value="11" onclick="fnCheckItem('11', '이태리어', 'for', this)">
											<label for="forItem11">이태리어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem18" title="터키어" value="18" onclick="fnCheckItem('18', '터키어', 'for', this)">
											<label for="forItem18">터키어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem06" title="라틴어" value="06" onclick="fnCheckItem('06', '라틴어', 'for', this)">
											<label for="forItem06">라틴어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem12" title="포르투갈어" value="12" onclick="fnCheckItem('12', '포르투갈어', 'for', this)">
											<label for="forItem12">포르투갈어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem13" title="화란어" value="13" onclick="fnCheckItem('13', '화란어', 'for', this)">
											<label for="forItem13">화란어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem14" title="힌디어(북부인도어)" value="14" onclick="fnCheckItem('14', '힌디어(북부인도어)', 'for', this)">
											<label for="forItem14">힌디어(북부인도어)</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem15" title="이란어" value="15" onclick="fnCheckItem('15', '이란어', 'for', this)">
											<label for="forItem15">이란어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem17" title="스와힐리어" value="17" onclick="fnCheckItem('17', '스와힐리어', 'for', this)">
											<label for="forItem17">스와힐리어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem19" title="마이인도네이사어" value="19" onclick="fnCheckItem('19', '마이인도네이사어', 'for', this)">
											<label for="forItem19">마이인도네이사어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem20" title="한국어" value="20" onclick="fnCheckItem('20', '한국어', 'for', this)">
											<label for="forItem20">한국어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem21" title="만주어" value="21" onclick="fnCheckItem('21', '만주어', 'for', this)">
											<label for="forItem21">만주어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem22" title="몽고어" value="22" onclick="fnCheckItem('22', '몽고어', 'for', this)">
											<label for="forItem22">몽고어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem23" title="스페인어" value="23" onclick="fnCheckItem('23', '스페인어', 'for', this)">
											<label for="forItem23">스페인어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem24" title="스웨덴어" value="24" onclick="fnCheckItem('24', '스웨덴어', 'for', this)">
											<label for="forItem24">스웨덴어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem25" title="체코어" value="25" onclick="fnCheckItem('25', '체코어', 'for', this)">
											<label for="forItem25">체코어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem26" title="덴마크어" value="26" onclick="fnCheckItem('26', '덴마크어', 'for', this)">
											<label for="forItem26">덴마크어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem27" title="네덜란드어" value="27" onclick="fnCheckItem('27', '네덜란드어', 'for', this)">
											<label for="forItem27">네덜란드어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem28" title="에스토니아어" value="28" onclick="fnCheckItem('28', '에스토니아어', 'for', this)">
											<label for="forItem28">에스토니아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem29" title="핀란드어" value="29" onclick="fnCheckItem('29', '핀란드어', 'for', this)">
											<label for="forItem29">핀란드어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem30" title="그리스어" value="30" onclick="fnCheckItem('30', '그리스어', 'for', this)">
											<label for="forItem30">그리스어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem31" title="헤브루어" value="31" onclick="fnCheckItem('31', '헤브루어', 'for', this)">
											<label for="forItem31">헤브루어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem32" title="헝가리어" value="32" onclick="fnCheckItem('32', '헝가리어', 'for', this)">
											<label for="forItem32">헝가리어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem33" title="아이슬란드어" value="33" onclick="fnCheckItem('33', '아이슬란드어', 'for', this)">
											<label for="forItem33">아이슬란드어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem34" title="라트비아어" value="34" onclick="fnCheckItem('34', '라트비아어', 'for', this)">
											<label for="forItem34">라트비아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem35" title="리투아니아어" value="35" onclick="fnCheckItem('35', '리투아니아어', 'for', this)">
											<label for="forItem35">리투아니아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem36" title="노르웨이어" value="36" onclick="fnCheckItem('36', '노르웨이어', 'for', this)">
											<label for="forItem36">노르웨이어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem37" title="폴란드어" value="37" onclick="fnCheckItem('37', '폴란드어', 'for', this)">
											<label for="forItem37">폴란드어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem38" title="루마니아어" value="38" onclick="fnCheckItem('38', '루마니아어', 'for', this)">
											<label for="forItem38">루마니아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem41" title="방글라데시어" value="41" onclick="fnCheckItem('41', '방글라데시어', 'for', this)">
											<label for="forItem41">방글라데시어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem42" title="바스크어" value="42" onclick="fnCheckItem('42', '바스크어', 'for', this)">
											<label for="forItem42">바스크어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem43" title="벨로루시어 " value="43" onclick="fnCheckItem('43', '벨로루시어 ', 'for', this)">
											<label for="forItem43">벨로루시어 </label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem44" title="카탈로니아어" value="44" onclick="fnCheckItem('44', '카탈로니아어', 'for', this)">
											<label for="forItem44">카탈로니아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem45" title="크로아티아어" value="45" onclick="fnCheckItem('45', '크로아티아어', 'for', this)">
											<label for="forItem45">크로아티아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem46" title="페로스어" value="46" onclick="fnCheckItem('46', '페로스어', 'for', this)">
											<label for="forItem46">페로스어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem47" title="페르시아어" value="47" onclick="fnCheckItem('47', '페르시아어', 'for', this)">
											<label for="forItem47">페르시아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem48" title="게일어" value="48" onclick="fnCheckItem('48', '게일어', 'for', this)">
											<label for="forItem48">게일어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem49" title="마세도니아어" value="49" onclick="fnCheckItem('49', '마세도니아어', 'for', this)">
											<label for="forItem49">마세도니아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem50" title="말타어" value="50" onclick="fnCheckItem('50', '말타어', 'for', this)">
											<label for="forItem50">말타어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem51" title="레토로만어" value="51" onclick="fnCheckItem('51', '레토로만어', 'for', this)">
											<label for="forItem51">레토로만어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem52" title="라플란드어" value="52" onclick="fnCheckItem('52', '라플란드어', 'for', this)">
											<label for="forItem52">라플란드어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem53" title="세르비아어" value="53" onclick="fnCheckItem('53', '세르비아어', 'for', this)">
											<label for="forItem53">세르비아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem54" title="슬로바키아어" value="54" onclick="fnCheckItem('54', '슬로바키아어', 'for', this)">
											<label for="forItem54">슬로바키아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem55" title="슬로베니아어" value="55" onclick="fnCheckItem('55', '슬로베니아어', 'for', this)">
											<label for="forItem55">슬로베니아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem56" title="소르비아어" value="56" onclick="fnCheckItem('56', '소르비아어', 'for', this)">
											<label for="forItem56">소르비아어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem57" title="수투어" value="57" onclick="fnCheckItem('57', '수투어', 'for', this)">
											<label for="forItem57">수투어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem58" title="총가어" value="58" onclick="fnCheckItem('58', '총가어', 'for', this)">
											<label for="forItem58">총가어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem59" title="츠와나어" value="59" onclick="fnCheckItem('59', '츠와나어', 'for', this)">
											<label for="forItem59">츠와나어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem60" title="우크라이나어" value="60" onclick="fnCheckItem('60', '우크라이나어', 'for', this)">
											<label for="forItem60">우크라이나어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem61" title="우르두어" value="61" onclick="fnCheckItem('61', '우르두어', 'for', this)">
											<label for="forItem61">우르두어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem62" title="벤다어" value="62" onclick="fnCheckItem('62', '벤다어', 'for', this)">
											<label for="forItem62">벤다어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem63" title="트란스카이어" value="63" onclick="fnCheckItem('63', '트란스카이어', 'for', this)">
											<label for="forItem63">트란스카이어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem64" title="이디시어" value="64" onclick="fnCheckItem('64', '이디시어', 'for', this)">
											<label for="forItem64">이디시어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem65" title="줄루어" value="65" onclick="fnCheckItem('65', '줄루어', 'for', this)">
											<label for="forItem65">줄루어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem66" title="미얀마어" value="66" onclick="fnCheckItem('66', '미얀마어', 'for', this)">
											<label for="forItem66">미얀마어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem67" title="라다크어" value="67" onclick="fnCheckItem('67', '라다크어', 'for', this)">
											<label for="forItem67">라다크어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem68" title="우즈베키스탄어" value="68" onclick="fnCheckItem('68', '우즈베키스탄어', 'for', this)">
											<label for="forItem68">우즈베키스탄어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem69" title="크메르어" value="69" onclick="fnCheckItem('69', '크메르어', 'for', this)">
											<label for="forItem69">크메르어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem70" title="카자흐어" value="70" onclick="fnCheckItem('70', '카자흐어', 'for', this)">
											<label for="forItem70">카자흐어</label>
										</span>
									
										<span>
											<input type="checkbox" name="forItem" id="forItem71" title="네팔어" value="71" onclick="fnCheckItem('71', '네팔어', 'for', this)">
											<label for="forItem71">네팔어</label>
										</span>
									
								</div>
							</div>

							<!-- 버튼 -->
							<a href="#none" class="closed" onclick="fn_show('jobForeignLang');">
								<span class="blind">팝업 닫기</span>
							</a>
							<!--// 버튼 -->
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">기타 우대사항</span>
					<div class="cont">
						<div class="box_chk-group flex_al view-col-3">
							
								<span>
									<input type="checkbox" name="computerPreferentialParam" id="computerPreferentialParam1" title="문서작성 (워드프로세스 활용)" value="1" onclick="resultCheckBoxTemplate('computerPreferentialParam');">
									<label for="computerPreferentialParam1">
										
											
											
												문서작성 (워드프로세스 활용)
											
										

									</label>
								</span>
							
								<span>
									<input type="checkbox" name="computerPreferentialParam" id="computerPreferentialParam2" title="표계산 (스프레드시트 활용)  " value="2" onclick="resultCheckBoxTemplate('computerPreferentialParam');">
									<label for="computerPreferentialParam2">
										
											
												스프레드시트(엑셀)
											
											
										

									</label>
								</span>
							
								<span>
									<input type="checkbox" name="computerPreferentialParam" id="computerPreferentialParam4" title="프레젠테이션 프로그램 활용" value="4" onclick="resultCheckBoxTemplate('computerPreferentialParam');">
									<label for="computerPreferentialParam4">
										
											
											
												프레젠테이션 프로그램 활용
											
										

									</label>
								</span>
							
								<span>
									<input type="checkbox" name="computerPreferentialParam" id="computerPreferentialParam6" title="회계프로그램" value="6" onclick="resultCheckBoxTemplate('computerPreferentialParam');">
									<label for="computerPreferentialParam6">
										
											
											
												회계프로그램
											
										

									</label>
								</span>
							
								<span>
									<input type="checkbox" name="computerPreferentialParam" id="computerPreferentialParam9" title="기타" value="9" onclick="resultCheckBoxTemplate('computerPreferentialParam');">
									<label for="computerPreferentialParam9">
										
											
											
												기타
											
										

									</label>
								</span>
							
							<span>
								<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParamA" value="A" onclick="f_disableEmpHopeANDEtcDisable('2');resultCheckBoxTemplate('pfMatterPreferentialParam');">
								<label for="pfMatterPreferentialParamA">장애인</label>
							</span>
							<span>
								<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParamB" value="B" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
								<label for="pfMatterPreferentialParamB">(준)고령자(50세이상)</label>
							</span>
							
								
									<span>
										<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParam05" title="차량소지자" value="05" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
										<label for="pfMatterPreferentialParam05">
										차량소지자
										</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParam14" title="운전면허증" value="14" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
										<label for="pfMatterPreferentialParam14">
										운전면허증
										</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParam10" title="북한이탈주민" value="10" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
										<label for="pfMatterPreferentialParam10">
										북한이탈주민
										</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParam09" title="장기복무 제대군인" value="09" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
										<label for="pfMatterPreferentialParam09">
										장기복무 제대군인
										</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParam07" title="고용촉진장려금대상자" value="07" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
										<label for="pfMatterPreferentialParam07">
										고용촉진장려금대상자
										</label>
									</span>
								
							
								
									<span>
										<input type="checkbox" name="pfMatterPreferentialParam" id="pfMatterPreferentialParam08" title="보훈취업지원대상자" value="08" onclick="resultCheckBoxTemplate('pfMatterPreferentialParam');">
										<label for="pfMatterPreferentialParam08">
										보훈취업지원대상자
										</label>
									</span>
								
							
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">마감일</span>
					<div class="cont">
						<div class="box_table_group box_datepicker">
							<div class="cell">
								<span class="box_ipt w_small"> <!-- D: /* 가로 사이즈 클래스 */ css 참조-->
									<input type="text" class="input_txt hasDatepicker" name="cloDateStdt_datepicker" id="cloDateStdt" title="마감일 시작날짜" placeholder="YYYY-MM-DD" inputmode="numeric"><button type="button" class="btn_calendar ui-datepicker-trigger" title="달력선택"></button><input name="cloDateStdt" type="hidden" data-type="datepicker">
								</span>
							</div>
							<i class="date_line">~</i>
							<div class="cell">
								<span class="box_ipt w_small"> <!-- D: /* 가로 사이즈 클래스 */ css 참조-->
									<input type="text" class="input_txt hasDatepicker" name="cloDateEndt_datepicker" id="cloDateEndt" title="마감일 종료날짜" placeholder="YYYY-MM-DD" inputmode="numeric"><button type="button" class="btn_calendar ui-datepicker-trigger" title="달력선택"></button><input name="cloDateEndt" type="hidden" data-type="datepicker">
								</span>
							</div>
						</div>
						<div class="box_table_group mt08">
							<span class="box_btn_group box_month_area ml0">
								<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn0');" id="cloTermSearchGbn0" name="cloTermSearchGbnParam" value="all" class="btn small type02 is-active" title="선택됨">초기화</button>
								
									<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn1');" id="cloTermSearchGbn1" name="cloTermSearchGbnParam" value="D-0" class="btn small type02 " title="">오늘</button>
								
									<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn2');" id="cloTermSearchGbn2" name="cloTermSearchGbnParam" value="D-1" class="btn small type02 " title="">내일</button>
								
									<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn3');" id="cloTermSearchGbn3" name="cloTermSearchGbnParam" value="D-3" class="btn small type02 " title="">3일</button>
								
									<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn4');" id="cloTermSearchGbn4" name="cloTermSearchGbnParam" value="W-1" class="btn small type02 " title="">1주 이내</button>
								
									<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn5');" id="cloTermSearchGbn5" name="cloTermSearchGbnParam" value="W-2" class="btn small type02 " title="">2주 이내</button>
								
									<button type="button" onclick="changeCloDateNew2(this.id);resultDateTemplate('마감일', 'cloDateStdt', 'cloDateEndt', 'cloTermSearchGbn6');" id="cloTermSearchGbn6" name="cloTermSearchGbnParam" value="M-1" class="btn small type02 " title="">한달</button>
								
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">등록일</span>
					<div class="cont">
						<div class="box_table_group box_datepicker">
							<div class="cell">
								<span class="box_ipt w_small"> <!-- D: /* 가로 사이즈 클래스 */ css 참조-->
									<input type="text" class="input_txt hasDatepicker" name="regDateStdt_datepicker" id="regDateStdt" title="등록일 시작날짜" placeholder="YYYY-MM-DD" inputmode="numeric"><button type="button" class="btn_calendar ui-datepicker-trigger" title="달력선택"></button><input name="regDateStdt" type="hidden" data-type="datepicker">
								</span>
							</div>
							<i class="date_line">~</i>
							<div class="cell">
								<span class="box_ipt w_small"> <!-- D: /* 가로 사이즈 클래스 */ css 참조-->
									<input type="text" class="input_txt hasDatepicker" name="regDateEndt_datepicker" id="regDateEndt" title="등록일 종료날짜" placeholder="YYYY-MM-DD" inputmode="numeric"><button type="button" class="btn_calendar ui-datepicker-trigger" title="달력선택"></button><input name="regDateEndt" type="hidden" data-type="datepicker">
								</span>
							</div>
						</div>
						<div class="box_table_group mt08">
							<span class="box_btn_group box_month_area ml0">
								<button type="button" onclick="changeDateNew2(this.id);resultDateTemplate('등록일','regDateStdt','regDateEndt','termSearchGbn0');" id="termSearchGbn0" name="termSearchGbnParam" value="all" class="btn small type02 is-active" title="선택됨">초기화</button>
								
									<button type="button" onclick="changeDateNew2(this.id);resultDateTemplate('등록일','regDateStdt','regDateEndt','termSearchGbn1');" id="termSearchGbn1" name="termSearchGbnParam" value="D-0" class="btn small type02 " title="">오늘</button>
								
									<button type="button" onclick="changeDateNew2(this.id);resultDateTemplate('등록일','regDateStdt','regDateEndt','termSearchGbn2');" id="termSearchGbn2" name="termSearchGbnParam" value="D-3" class="btn small type02 " title="">3일</button>
								
									<button type="button" onclick="changeDateNew2(this.id);resultDateTemplate('등록일','regDateStdt','regDateEndt','termSearchGbn3');" id="termSearchGbn3" name="termSearchGbnParam" value="W-1" class="btn small type02 " title="">1주 이내</button>
								
									<button type="button" onclick="changeDateNew2(this.id);resultDateTemplate('등록일','regDateStdt','regDateEndt','termSearchGbn4');" id="termSearchGbn4" name="termSearchGbnParam" value="W-2" class="btn small type02 " title="">2주 이내</button>
								
									<button type="button" onclick="changeDateNew2(this.id);resultDateTemplate('등록일','regDateStdt','regDateEndt','termSearchGbn5');" id="termSearchGbn5" name="termSearchGbnParam" value="M-1" class="btn small type02 " title="">한달</button>
								
							</span>
						</div>
					</div>
				</li>
				<li>
					<span class="tit b1_sb">정보제공처</span>
					<div class="cont">
						<div class="box_chk-group flex_al view-col-3">
                        	<span>
								<input type="checkbox" id="b_siteClcdall" name="b_siteClcd" value="all" onclick="fn_siteClcdGbn('all')" checked="checked">
								<label for="b_siteClcdall">전체</label>
							</span>

							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdWORK" name="b_siteClcd" value="WORK" onclick="fn_siteClcdGbn('WORK')">
									<label for="b_siteClcdWORK">고용24</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdGOJ" name="b_siteClcd" value="GOJ" onclick="fn_siteClcdGbn('GOJ')">
									<label for="b_siteClcdGOJ">나라일터</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdALI" name="b_siteClcd" value="ALI" onclick="fn_siteClcdGbn('ALI')">
									<label for="b_siteClcdALI">알리오</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdWIH" name="b_siteClcd" value="WIH" onclick="fn_siteClcdGbn('WIH')">
									<label for="b_siteClcdWIH">여성기업일자리허브</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCLE" name="b_siteClcd" value="CLE" onclick="fn_siteClcdGbn('CLE')">
									<label for="b_siteClcdCLE">클린아이</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdMMA" name="b_siteClcd" value="MMA" onclick="fn_siteClcdGbn('MMA')">
									<label for="b_siteClcdMMA">병역일터</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCJK" name="b_siteClcd" value="CJK" onclick="fn_siteClcdGbn('CJK')">
									<label for="b_siteClcdCJK">잡코리아</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCSI" name="b_siteClcd" value="CSI" onclick="fn_siteClcdGbn('CSI')">
									<label for="b_siteClcdCSI">사람인</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCIN" name="b_siteClcd" value="CIN" onclick="fn_siteClcdGbn('CIN')">
									<label for="b_siteClcdCIN">인크루트</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCCN" name="b_siteClcd" value="CCN" onclick="fn_siteClcdGbn('CCN')">
									<label for="b_siteClcdCCN">커리어</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCMJ" name="b_siteClcd" value="CMJ" onclick="fn_siteClcdGbn('CMJ')">
									<label for="b_siteClcdCMJ">미디어잡</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdOEW" name="b_siteClcd" value="OEW" onclick="fn_siteClcdGbn('OEW')">
									<label for="b_siteClcdOEW">공채속보</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdMIT" name="b_siteClcd" value="MIT" onclick="fn_siteClcdGbn('MIT')">
									<label for="b_siteClcdMIT">마이다스인</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCPR" name="b_siteClcd" value="CPR" onclick="fn_siteClcdGbn('CPR')">
									<label for="b_siteClcdCPR">팜리크루트</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdWFC" name="b_siteClcd" value="WFC" onclick="fn_siteClcdGbn('WFC')">
									<label for="b_siteClcdWFC">한국사회보장정보원</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdIBK" name="b_siteClcd" value="IBK" onclick="fn_siteClcdGbn('IBK')">
									<label for="b_siteClcdIBK">i-ONE JOB</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdPRD" name="b_siteClcd" value="PRD" onclick="fn_siteClcdGbn('PRD')">
									<label for="b_siteClcdPRD">알앤디잡</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdKOS" name="b_siteClcd" value="KOS" onclick="fn_siteClcdGbn('KOS')">
									<label for="b_siteClcdKOS">중소벤처기업진흥공단</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCAT" name="b_siteClcd" value="CAT" onclick="fn_siteClcdGbn('CAT')">
									<label for="b_siteClcdCAT">캐치</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCWT" name="b_siteClcd" value="CWT" onclick="fn_siteClcdGbn('CWT')">
									<label for="b_siteClcdCWT">원티드</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCDM" name="b_siteClcd" value="CDM" onclick="fn_siteClcdGbn('CDM')">
									<label for="b_siteClcdCDM">디맨드</label>
								</span>
							
								
								
									
									
								
								<span>
									<input type="checkbox" id="b_siteClcdCWK" name="b_siteClcd" value="CWK" onclick="fn_siteClcdGbn('CWK')">
									<label for="b_siteClcdCWK">건설워커</label>
								</span>
							
						</div>
					</div>
				</li>
				<li>
					<ul class="box_list_area wd100per">
						<li class="txt_list">
							<strong>『고용상 연령차별금지 및 고령자 고용촉진에 관한 법률』 이 시행됨에 따라 <span class="point_color">채용정보에서 연령이 삭제</span>되었습니다.</strong>
						</li>
							
						<li class="txt_list">
							<strong>
								<span class="point_color">취업사기 방지</span></strong>를 위한 특별안내 <button type="button" class="btn small type02" onclick="fn_showPreventLayer(this);">자세히보기</button>
						</li>
					</ul>
				</li>
			</ul>
		</div>

		<div class="box_btn_wrap mt24">
			<button type="button" id="moreBtn" class="btn large type02 w100 btn_slide_more on" onclick="WkComLib.moveScrollTop(this)">
				
					
					
						
					
				
				추가 검색조건<span class="txt">열기</span>
			</button>
		</div>
	</article>
<form id="mForm" name="mForm" action="/wk/a/b/1200/retriveDtlEmpSrchListInPost.do" method="POST" novalidate="novalidate">
	<input id="currentPageNo" name="currentPageNo" type="hidden" value="1">
	<input type="hidden" name="moreButtonYn" value="">
	<input type="hidden" name="mode" id="mode" value="">
	<input type="hidden" name="searchMode" id="searchMode" value="">
	<input type="hidden" name="entryRoute" id="entryRoute" value="">
	<input type="hidden" name="seqNo" id="seqNo" value="">
	<input type="hidden" name="eventNo" id="eventNo" value="">
	<input type="hidden" name="basicSetupYnChk" id="basicSetupYnChk" value="">
	<input type="hidden" name="basicSetupYn" id="basicSetupYn" value="">

	<input type="hidden" id="resultCnt" name="resultCnt" value="10">
	<input type="hidden" id="sortOrderBy" name="sortOrderBy" value="DESC">
	<input type="hidden" id="sortField" name="sortField" value="DATE">
	<input type="hidden" id="viewType" name="viewType" value="">

	<input type="hidden" id="pageIndex" name="pageIndex" value="1">
	<input type="hidden" id="occupation" name="occupation" value="">
	<input type="hidden" id="region" name="region" value="">
	<input type="hidden" id="keyword" name="keyword" value="">
	<input type="hidden" id="keywordWantedTitle" name="keywordWantedTitle" value="N">
	<input type="hidden" id="keywordBusiNm" name="keywordBusiNm" value="N">
	<input type="hidden" id="keywordJobCont" name="keywordJobCont" value="N">
	<input type="hidden" id="keywordStaAreaNm" name="keywordStaAreaNm" value="N">
	<input type="hidden" id="payGbn" name="payGbn" value="">
	<input type="hidden" id="minPay" name="minPay" value="">
	<input type="hidden" id="maxPay" name="maxPay" value="">
	<input type="hidden" id="careerTypes" name="careerTypes" value="">
	<input type="hidden" id="careerTo" name="careerTo" value="">
	<input type="hidden" id="careerFrom" name="careerFrom" value="">
	<input type="hidden" id="academicGbn" name="academicGbn" value="">
	<input type="hidden" id="academicGbnoEdu" name="academicGbnoEdu" value="">
	<input type="hidden" id="siteClcd" name="siteClcd" value="all">

	<input type="hidden" name="staArea" id="staArea" value="">
	<input type="hidden" name="indArea" id="indArea" value="">
	<input type="hidden" name="templateInfo" id="templateInfo" value="">
	<input type="hidden" name="codeDepth1Info" id="codeDepth1Info" value="11000">
	<input type="hidden" name="codeDepth2Info" id="codeDepth2Info" value="11000">
	<input type="hidden" name="depth2SelCode" id="depth2SelCode" value="">
	<input type="hidden" name="templateDepthNoInfo" id="templateDepthNoInfo" value="">
	<input type="hidden" name="templateDepthNmInfo" id="templateDepthNmInfo" value="">
	<input type="hidden" name="benefitSrchAndOr" id="benefitSrchAndOr" value="O">

	<input type="hidden" name="keywordJobCd" id="keywordJobCd" value="">
	<input type="hidden" name="keywordJobCdSeqNo" id="keywordJobCdSeqNo" value="">
	<input type="hidden" name="keywordEtcYn" id="keywordEtcYn" value="">
	<input type="hidden" name="exJobsCd" id="exJobsCd" value="">
	<input type="hidden" name="keywordFlag" id="keywordFlag" value="">
	
	<input type="hidden" name="station" id="station" value="">
	<input type="hidden" name="stationNm" id="stationNm" value="">
	<input type="hidden" name="employGbn" id="employGbn" value="">
	<input type="hidden" name="termContractMmcnt" id="termContractMmcnt" value="">
	<input type="hidden" name="subEmpHopeYn" id="subEmpHopeYn" value="">
	<input type="hidden" name="enterPriseGbn" id="enterPriseGbn" value="">
	<input type="hidden" name="holidayGbn" id="holidayGbn" value="">
	<input type="hidden" name="preferentialGbn" id="preferentialGbn" value="">
	<input type="hidden" name="cloDateStdtParam" id="cloDateStdtParam" value="">
	<input type="hidden" name="cloDateEndtParam" id="cloDateEndtParam" value="">
	<input type="hidden" name="emailApplyYn" id="emailApplyYn" value="">
	<input type="hidden" name="regDateStdtParam" id="regDateStdtParam" value="">
	<input type="hidden" name="regDateEndtParam" id="regDateEndtParam" value="">
	<input type="hidden" name="termSearchGbn" id="termSearchGbn" value="">
	<input type="hidden" name="cloTermSearchGbn" id="cloTermSearchGbn" value="">

	<input type="hidden" id="benefitGbn" name="benefitGbn" value="">
	<input type="hidden" id="rot2WorkYn" name="rot2WorkYn" value="">
	<input type="hidden" id="rot3WorkYn" name="rot3WorkYn" value="">
	<input type="hidden" id="mealOfferClcd" name="mealOfferClcd" value="">
	<input type="hidden" id="empTpGbcd" name="empTpGbcd" value="1">
	<input type="hidden" id="disableEmpHopeGbn" name="disableEmpHopeGbn" value="">
	<input type="hidden" id="actServExcYn" name="actServExcYn" value="">
	<input type="hidden" id="resrDutyExcYn" name="resrDutyExcYn" value="">
	<input type="hidden" id="publDutyExcYn" name="publDutyExcYn" value="">
	<input type="hidden" id="cert" name="cert" value="">

	<input type="hidden" id="major" name="major" value="">
	<input type="hidden" id="foriegn" name="foriegn" value="">
	<input type="hidden" id="computerPreferential" name="computerPreferential" value="">
	<input type="hidden" id="pfMatterPreferential" name="pfMatterPreferential" value="">
	<input type="hidden" id="laborHrShortYn" name="laborHrShortYn" value="">
	<input type="hidden" id="essCertChk" name="essCertChk" value="N">

	<input type="hidden" id="birthFromYY" name="birthFromYY" value="">
	<input type="hidden" id="birthToYY" name="birthToYY" value="">



	<input type="hidden" id="carrEssYns" name="carrEssYns" value="">
	<input type="hidden" id="eodwYn" name="eodwYn" value="">
	<input type="hidden" id="tlmgYn" name="tlmgYn" value="">
	<input type="hidden" id="shsyWorkSecd" name="shsyWorkSecd" value="">
	<input type="hidden" id="infaYn" name="infaYn" value="">


	<input type="hidden" id="cloTermSearchGbnParamChecker" value="">
	<input type="hidden" id="termSearchGbnParamChecker" value="">

	<input type="hidden" id="hidSrcKeyword" name="srcKeyword" value="">
	<input type="hidden" id="hidNotSrcKeyword" name="notSrcKeyword" value="">
	<div data-include="floating_result_inc">
		<!-- 레이어 : 플로팅 검색결과(20250224 수정) -->
		<div class="floating_search_result ty2 mt16 active" style="z-index: 1;">
			<div class="box_border_type type_pd24 pb16">
				<div class="line_type">
					<article class="inner_wrap">
						<h3 class="tit">검색조건<strong class="clr_blue" id="selectedIdTitle"> 1건</strong></h3>
						<div class="floating_result_section" id="selectedId">
						
		<span id="empTpGbcdParamNm1" class="btn_hash medium type02 r30 templListInfo">상용직<button type="button" class="ico16_delete" onclick="fnRemoveCheckNm('1', 'empTpGbcdParam'); return false"><span class="blind">상용직 삭제</span></button></span>
	</div>
					</article>
				</div>
				<div class="line_type pt16 flex_box flex_js_s">
					<ul class="rslt_btn_box ty2">
						<li>
							<a href="#none" class="b1_r back" onclick="fn_SearchReset();">초기화</a>
						</li>
						<li>
							<a href="#none" class="b1_r disk" onclick="fn_Save();">맞춤정보 저장</a>
						</li>
						<li>
							<a href="#none" class="b1_r folder" id="layerDialogCloseFocus" onclick="fn_Setup();">맞춤정보 불러오기</a>
						</li>
						<!--
						<li>
							<a href="javascript:void(0)" class="b1_r setting">맞춤정보 관리</a>
						</li>
						-->
					</ul>
					<button type="button" onclick="fn_Search('1');" class="btn large type01 fill wd180px"><span>검색</span></button>
				</div>

			</div>
		</div>
		<!-- // 레이어 : 플로팅 검색결과(20250224) -->
	</div>
	

	<div class="box_group_wrap">
		<!-- tableArea -->
		<div class="box_table_wrap">
			<div class="box_table_hd">
				<div class="section_left">
					<button type="button" class="btn medium type01" onclick="f_empCompare();">채용정보 비교검색</button>
					<span class="tit ml08">검색건수 <span class="txt_total">124,197</span>건</span>
				</div>

				<div class="section_right">
	            	<span class="sel round">
						<select title="리스트 보기 정렬기준을 선택해 주세요" onchange="sortOption(this.value);">
							<option value="DATE|DESC" selected"="">최근등록일순</option>
							<option value="DATE|ASC">예전등록일순</option>
							<option value="comnm|ASC">회사명(ㄱ→ㅎ)</option>
							<option value="comnm|DESC">회사명(ㅎ→ㄱ)</option>
							<option value="mmSal|DESC">임금높은순</option>
							<option value="mmSal|ASC">임금낮은순</option>
							<option value="edu|DESC">학력높은순</option>
							<option value="edu|ASC">학력낮은순</option>
							<option value="careerSort|DESC">경력많은순</option>
							<option value="careerSort|ASC">경력적은순</option>
							<option value="receiptCloseDt|ASC">마감일순(오늘~)</option>
							<option value="receiptCloseDt|DESC">마감일순(상시~)</option>
						</select>
					</span>
					<span class="sel round">
						<select title="리스트보기 개수를 선택해 주세요" onchange="$('#resultCnt').val(this.value);">
							<option value="10" selected="">10개</option>
							<option value="30">30개</option>
							<option value="50">50개</option>
						</select>
					</span>
					<button type="button" class="btn btn_round type02" onclick="fn_Search(1);">적용</button>
					
				</div>
			</div>

			<!-- table : l_type02 -->
			<table class="box_table type_pd24" id="contentArea"><caption>
						회사명 / 채용공고명 / 정보제공처
						,지원자격 / 근무조건
						,마감 / 등록일을(를) 제공하는 표</caption>
				
				<colgroup>
					<col>
					<col style="width:40%">
					<col style="width:18%">
				</colgroup>
				<thead>
				<tr>
					<th scope="col">
						회사명 / 채용공고명 / 정보제공처
						<div class="box_tooltip">
							<button type="button" class="btn_help dis"><span class="blind">도움말</span></button>
							<div class="box_help-data pd12 w_big">
								<p class="s1_sb">기업형태</p>
								<ul class="box_calc_wrap col-3">
									<li class="cell">
										<span class="tbl_label blue">대기업</span> 대기업
									</li>
									<li class="cell">
										<span class="tbl_label gray">공공</span> 공기업/ 공공기관
									</li>
									<li class="cell">
										<span class="tbl_label purple">외국계</span> 외국계기업
									</li>
									<li class="cell">
										<span class="tbl_label orange">코스피</span> 코스피
									</li>
									<li class="cell">
										<span class="tbl_label red">코스닥</span> 코스닥
									</li>
									<li class="cell">
										<span class="tbl_label yellow">일학습</span> 일학습병행기업
									</li>
									<li class="cell">
										<span class="tbl_label green2">청년일자리강소기업</span>
									</li>
									<li class="cell">
										<span class="tbl_label brown">가족</span> 가족친화기업
									</li>
									<li class="cell">
										<span class="tbl_label brown">중견</span> 중견기업
									</li>
								</ul>
								<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
								</button>
							</div>
						</div>
					</th>
					<th scope="col">지원자격 / 근무조건
						<div class="box_tooltip">
							<button type="button" class="btn_help dis"><span class="blind">도움말</span></button>
							<div class="box_help-data w_big">
								<p class="s1_sb">고용형태</p>
								<ul class="box_list_area">
									<li class="txt_list">정규 : 기간의 정함이 없는 근로계약</li>
									<li class="txt_list">비정규 : 기간의 정함이 있는 근로계약</li>
									<li class="txt_list">시간(단기) : 기간의 정함이 있는 근로계약(시간(선택)제)</li>
									<li class="txt_list">시간(장기) : 기간의 정함이 없는 근로계약(시간(선택)제)</li>
									<li class="txt_list">파견 : 파견근로</li>
									<li class="txt_list">대체 : 대체인력채용</li>
								</ul>
								<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
								</button>
							</div>
						</div>
					</th>
					<th scope="col">마감 / 등록일</th>
				</tr>
				</thead>
				<tbody>
				
					<tr id="list1">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo0" value="K131212509020040|VALIDATION|울산노인의집|사회복지시설 세탁 및 청소 주3일 근무자 1명 모집" title="울산노인의집 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('6208204941');">
															울산노인의집
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K131212509020040&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														사회복지시설 세탁 및 청소 주3일 근무자 1명 모집
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K131212509020040', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K131212509020040', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
															
															
																시급
															
														
														
														
														
														
														
															
															
																10,030
															
														
														원
														
														
														
														
															~
															
																
																
																	10,030
																
															
															원
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													
													
													
													주3일
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 21시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												09:00 ~ 17:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														울산광역시 울주군 삼동면 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo0">D-14</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-09-16';
									var closeDt = '25/09/16';
									var closeTpNm = '';
									var wantedYn = 'N';
									var index = '0';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-09-16</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list2">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo1" value="K150112509020019|VALIDATION|현대경희한의원|함께하실 간호조무사님 모십니다." title="현대경희한의원 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('1209912240');">
															현대경희한의원
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K150112509020019&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														함께하실 간호조무사님 모십니다.
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K150112509020019', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K150112509020019', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		235
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													
													주6일
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 43시간 근로</span>
											
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														인천광역시 부평구 경원대로 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo1">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'Y';
									var index = '1';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list3">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo2" value="KJ22032509020001|VALIDATION|고령요양원|★고령군 일자리·청년창업 지원센터★ 고령요양원 주간/ 주야요양보호사 채용" title="고령요양원 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('5048281326');">
															고령요양원
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KJ22032509020001&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
														★고령군 일자리·청년창업 지원센터★ 고령요양원 주간/ 주야요양보호사...
													
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KJ22032509020001', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KJ22032509020001', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		209
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 40시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												09:00 ~ 18:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경상북도 고령군 대가야읍 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo2">D-42</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-10-14';
									var closeDt = '25/10/14';
									var closeTpNm = '';
									var wantedYn = 'N';
									var index = '2';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-10-14</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list4">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo3" value="K170082509020006|VALIDATION|(주)이에스그린|폐기물 중간처리장 포크레인 기사 모집" title="(주)이에스그린 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('1648600462');">
															(주)이에스그린
														</a>
													
												
												<span class="label_box ml08">
													
													<span class="tbl_label brown">가족</span>
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K170082509020006&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														폐기물 중간처리장 포크레인 기사 모집
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K170082509020006', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K170082509020006', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		330
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
													
														
													
												
												
													경력3년
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 40시간 근로</span>
											
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														세종특별자치시 부강면 부강행산로 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo3">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'Y';
									var index = '3';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list5">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo4" value="KEC0112509020006|VALIDATION|주식회사조은기업|★현대중공업 내 신호수모집(경총 중장년내일센터 채용대행)" title="주식회사조은기업 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('7398702387');">
															주식회사조은기업
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KEC0112509020006&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														★현대중공업 내 신호수모집(경총 중장년내일센터 채용대행)
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KEC0112509020006', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KEC0112509020006', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		350
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
													
														
													
												
												
													경력1년
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													
													주6일
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 48시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												08:00 ~ 18:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														울산광역시 동구 방어진순환도로 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo4">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'Y';
									var index = '4';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list6">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo5" value="K131212509020039|VALIDATION|성연어린이집|성연어린이집 보조교사 채용" title="성연어린이집 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('6208003633');">
															성연어린이집
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K131212509020039&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														성연어린이집 보조교사 채용
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K131212509020039', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K131212509020039', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		110
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																대졸(2~3년)
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 20시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												09:00 ~ 13:30
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														울산광역시 중구 계변고개 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo5">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'Y';
									var index = '5';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list7">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo6" value="K170062509020008|VALIDATION|의료법인주은복지의료재단|주은라파스요양병원 급식 조리원 채용" title="의료법인주은복지의료재단 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('3078206328');">
															의료법인주은복지의료재단
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K170062509020008&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														주은라파스요양병원 급식 조리원 채용
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K170062509020008', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K170062509020008', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		330
																	
																	
																
															
															
														
														만원
														
														
														
														
															~
															
																
																	
																	
																		
																			330
																		
																		
																	
																
																
															
															만원
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 40시간 근로</span>
											
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														충청남도 공주시 탄천면 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo6">D-28</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-09-30';
									var closeDt = '25/09/30';
									var closeTpNm = '';
									var wantedYn = 'N';
									var index = '6';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-09-30</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list8">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo7" value="KJ21022509020013|VALIDATION|디티에스코리아주식회사|화서역푸르지오 브리시엘 아파트 경비대원 모집" title="디티에스코리아주식회사 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('1438131513');">
															디티에스코리아주식회사
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KJ21022509020013&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														화서역푸르지오 브리시엘 아파트 경비대원 모집
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KJ21022509020013', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KJ21022509020013', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		305
																	
																	
																
															
															
														
														만원
														
														
														
														
															~
															
																
																	
																	
																		
																			305
																		
																		
																	
																
																
															
															만원
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													
													
													주4일
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 40시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												08:00 ~ 08:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경기도 수원시 장안구 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo7">D-60</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'N';
									var index = '7';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list9">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo8" value="K151642509020007|VALIDATION|주식회사케이알테크|제조업체 생산부 직원을 모집합니다. (검사및 사상, 포장)" title="주식회사케이알테크 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('1268600932');">
															주식회사케이알테크
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K151642509020007&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														제조업체 생산부 직원을 모집합니다. (검사및 사상, 포장)
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K151642509020007', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K151642509020007', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		210
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																고졸
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 40시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												09:00 ~ 18:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경기도 하남시 초광산단동로6번길 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo8">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'Y';
									var index = '8';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							
						</td>
					</tr>
				
					<tr id="list10">
						<td class="al_left pd24">
							<div class="box_table_group gap_box08 column">
								<div class="cell">
									<div class="box_chk-group">
										<label>
											<span>
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo9" value="K131332509020028|VALIDATION|다올 마루|2025 다올마루 신입사원 모집" title="다올 마루 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('5496300266');">
															다올 마루
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K131332509020028&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														2025 다올마루 신입사원 모집
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K131332509020028', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K131332509020028', 'tb_workinfoworknet', 'VAL'); return false;">
												<i class="ico24_search ico16"></i>
												<span class="blind">요약보기</span>
											</button>
										</span>
									</p>
								</div>
							</div>
						</td>
						<td class="link pd24">
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="dollar">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item b1_sb">
												
													
														
															
															
																월급
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		280
																	
																	
																
															
															
														
														만원
														
														
														
														
															~
															
																
																	
																	
																		
																			300
																		
																		
																	
																
																
															
															만원
														
													
													
													
												
											</span>
											
												
													<span class="item b1_sb">상여별도&nbsp;30%</span>
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													경력무관
												
											</span>
											

											
											<span class="item sm">
												
													
													
														
															
															
																학력무관
															
														
													
												
											</span>
											
										</p>
									</li>
									

									
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											
											<span class="item sm 2">
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 48시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												07:30 ~ 06:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경상남도 양산시 동면 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo9">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-10-31';
									var closeDt = '25/10/31';
									var closeTpNm = '';
									var wantedYn = 'Y';
									var index = '9';
									var FORMAT = "-";

									if (date.length != 10)
										return null;

									if (date.indexOf(FORMAT) < 0)
										return null;

									if(date.substring(0,4) == '2099'){
										$("#dDayInfo"+index).text('채용시까지');
										return;
									}else if(wantedYn == 'Y'){
										$("#dDayInfo"+index).html('채용시까지');
										return;
									}
									var from_dt = DateLib.getToday();
									var to_dt = DateLib.getDay(date, "YYYYMMDD");
									var returnData = DateLib.diffDay(from_dt, to_dt);

									if(returnData < 0 ){
										$("#dDayInfo"+index).text('마감');
									}else if(returnData == 1){
										$("#dDayInfo"+index).text('D-'+returnData);
									}else if(returnData == 0){
										$("#dDayInfo"+index).html('오늘마감');
									}else{
										$("#dDayInfo"+index).text('D-'+returnData);
									}
								});
							</script>
							
							<p class="s1_r">마감일 : 2025-10-31</p>
							
							<p class="s1_r">등록일 : 2025-09-02</p>
							<input type="hidden" id="listTotCnt" value="9">
						</td>
					</tr>
				
				
				</tbody>
			</table>
			<!-- //table -->

			<!-- pagination -->
			<div class="section_bottom">
				<div class="box_pagination">
					<div class="set_pagination"><div class="box_pagination"><button type="button" class="btn_page first" onclick="fn_Move(1); return false;"><span class="blind">처음으로 가기</span></button>&nbsp;<button type="button" class="btn_page prev" onclick="fn_Move(1); return false;"><span class="blind">이전</span></button>&nbsp;<button type="button" class="active" title="1 페이지 이동" aria-current="true">1</button>  &nbsp;<button type="button" onclick="fn_Move(2); return false;" title="2 페이지 이동">2</button>&nbsp;<button type="button" onclick="fn_Move(3); return false;" title="3 페이지 이동">3</button>&nbsp;<button type="button" onclick="fn_Move(4); return false;" title="4 페이지 이동">4</button>&nbsp;<button type="button" onclick="fn_Move(5); return false;" title="5 페이지 이동">5</button>&nbsp;<button type="button" onclick="fn_Move(6); return false;" title="6 페이지 이동">6</button>&nbsp;<button type="button" onclick="fn_Move(7); return false;" title="7 페이지 이동">7</button>&nbsp;<button type="button" onclick="fn_Move(8); return false;" title="8 페이지 이동">8</button>&nbsp;<button type="button" onclick="fn_Move(9); return false;" title="9 페이지 이동">9</button>&nbsp;<button type="button" onclick="fn_Move(10); return false;" title="10 페이지 이동">10</button>&nbsp;<button type="button" class="btn_page next" onclick="fn_Move(11); return false;"><span class="blind">다음</span></button>&nbsp;<button type="button" class="btn_page last" onclick="fn_Move(12420); return false;"><span class="blind">마지막으로 가기</span></button>&nbsp;</div></div>
					
				</div>
			</div>
			<!-- //pagination -->
		</div>
	</div>
</form></div>


3. Click on the 직종선택 button (Category Filter section): 
<button type="button" class="btn medium mw_auto type02" onclick="fn_show('jobCategory');"><span>직종선택</span></button>
4. Then we will have this 1st filter, 2nd filter, 3rd filter. HTML:
<div id="jobCategory" style="" class="layer_section on">
<!-- 본문 컨텐츠 -->
<!-- 250416 article 태그 삭제 -->
<ul class="box_list_area">
    <li class="txt_list">직종 : 최대 10개의 직종 선택이 가능합니다. 원하시는 직종을 선택하세요.</li>
    <li class="txt_list">체크박스를 클릭하면 직종이 선택되고, ‘직종명’을 클릭하면 하위 분류가 보여집니다.</li>
    <li class="txt_list">3차 분류 직종을 선택하시면 해당 직종에 대한 키워드로 채용정보를 검색하실 수 있습니다.</li>
</ul>
<table class="search_table mt16"><caption>검색키워드을(를) 제공하는 표</caption>
    <colgroup>
        <col style="width:16%;">
        <col>
    </colgroup>
    <tbody>
    <tr>
        <th scope="row"><span>검색키워드</span></th>
        <td>
            <div class="box_sch_group">
                    <span class="box_ipt">
                        <input type="text" id="jobSearchKeyword" name="" class="input_txt" title="직종 키워드를 입력해 주세요. 예) 영업,운전, 사무" value="" placeholder="직종 키워드를 입력해 주세요. 예) 영업,운전, 사무">
                        <button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
                    </span>
                <button type="button" class="btn medium fill type01" onclick="jobCategorySearch();">검색</button>
            </div>
        </td>
    </tr>
    </tbody>
</table>

<div id="wk-jobs-search-view1">
    <div class="list_chk_area type_col chk_col_type mt16">
        <div class="col">
            <p class="tit">1차 분류</p>
            <div class="cont_area scroll h280">
                <ul class="box_chk-group chk_row" id="mainJobDiv"><li><span class="pt08"><input type="checkbox" id="chk08" name="mainJob" title="건설·채굴 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'08');" value="08"><label for="chk08"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName08" title="건설·채굴에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('08', 'mainJob0' , 'subJob');">건설·채굴</button><input type="hidden" id="mainJob0Nm" value="건설·채굴"><input type="hidden" name="firstJobName" id="jobName08" value="건설·채굴"></li><li><span class="pt08"><input type="checkbox" id="chk01" name="mainJob" title="경영·사무·금융·보험 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'01');" value="01"><label for="chk01"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName01" title="경영·사무·금융·보험에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('01', 'mainJob1' , 'subJob');">경영·사무·금융·보험</button><input type="hidden" id="mainJob1Nm" value="경영·사무·금융·보험"><input type="hidden" name="firstJobName" id="jobName01" value="경영·사무·금융·보험"></li><li><span class="pt08"><input type="checkbox" id="chk03" name="mainJob" title="교육·법률·사회복지·경찰·소방 및 군인 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'03');" value="03"><label for="chk03"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName03" title="교육·법률·사회복지·경찰·소방 및 군인에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('03', 'mainJob2' , 'subJob');">교육·법률·사회복지·경찰·소방 및 군인</button><input type="hidden" id="mainJob2Nm" value="교육·법률·사회복지·경찰·소방 및 군인"><input type="hidden" name="firstJobName" id="jobName03" value="교육·법률·사회복지·경찰·소방 및 군인"></li><li><span class="pt08"><input type="checkbox" id="chk13" name="mainJob" title="농림어업직 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'13');" value="13"><label for="chk13"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName13" title="농림어업직에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('13', 'mainJob3' , 'subJob');">농림어업직</button><input type="hidden" id="mainJob3Nm" value="농림어업직"><input type="hidden" name="firstJobName" id="jobName13" value="농림어업직"></li><li><span class="pt08"><input type="checkbox" id="chk06" name="mainJob" title="미용·여행·숙박·음식·경비·돌봄·청소 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'06');" value="06"><label for="chk06"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName06" title="미용·여행·숙박·음식·경비·돌봄·청소에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('06', 'mainJob4' , 'subJob');">미용·여행·숙박·음식·경비·돌봄·청소</button><input type="hidden" id="mainJob4Nm" value="미용·여행·숙박·음식·경비·돌봄·청소"><input type="hidden" name="firstJobName" id="jobName06" value="미용·여행·숙박·음식·경비·돌봄·청소"></li><li><span class="pt08"><input type="checkbox" id="chk04" name="mainJob" title="보건·의료 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'04');" value="04"><label for="chk04"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName04" title="보건·의료에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('04', 'mainJob5' , 'subJob');">보건·의료</button><input type="hidden" id="mainJob5Nm" value="보건·의료"><input type="hidden" name="firstJobName" id="jobName04" value="보건·의료"></li><li><span class="pt08"><input type="checkbox" id="chk09" name="mainJob" title="설치·정비·생산-기계·금속·재료 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'09');" value="09"><label for="chk09"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName09" title="설치·정비·생산-기계·금속·재료에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('09', 'mainJob6' , 'subJob');">설치·정비·생산-기계·금속·재료</button><input type="hidden" id="mainJob6Nm" value="설치·정비·생산-기계·금속·재료"><input type="hidden" name="firstJobName" id="jobName09" value="설치·정비·생산-기계·금속·재료"></li><li><span class="pt08"><input type="checkbox" id="chk12" name="mainJob" title="설치·정비·생산-인쇄·목재·공예 및 제조 단순 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'12');" value="12"><label for="chk12"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName12" title="설치·정비·생산-인쇄·목재·공예 및 제조 단순에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('12', 'mainJob7' , 'subJob');">설치·정비·생산-인쇄·목재·공예 및 제조 단순</button><input type="hidden" id="mainJob7Nm" value="설치·정비·생산-인쇄·목재·공예 및 제조 단순"><input type="hidden" name="firstJobName" id="jobName12" value="설치·정비·생산-인쇄·목재·공예 및 제조 단순"></li><li><span class="pt08"><input type="checkbox" id="chk10" name="mainJob" title="설치·정비·생산-전기·전자·정보통신 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'10');" value="10"><label for="chk10"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName10" title="설치·정비·생산-전기·전자·정보통신에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('10', 'mainJob8' , 'subJob');">설치·정비·생산-전기·전자·정보통신</button><input type="hidden" id="mainJob8Nm" value="설치·정비·생산-전기·전자·정보통신"><input type="hidden" name="firstJobName" id="jobName10" value="설치·정비·생산-전기·전자·정보통신"></li><li><span class="pt08"><input type="checkbox" id="chk11" name="mainJob" title="설치·정비·생산-화학·환경·섬유·의복·식품가공 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'11');" value="11"><label for="chk11"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName11" title="설치·정비·생산-화학·환경·섬유·의복·식품가공에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('11', 'mainJob9' , 'subJob');">설치·정비·생산-화학·환경·섬유·의복·식품가공</button><input type="hidden" id="mainJob9Nm" value="설치·정비·생산-화학·환경·섬유·의복·식품가공"><input type="hidden" name="firstJobName" id="jobName11" value="설치·정비·생산-화학·환경·섬유·의복·식품가공"></li><li><span class="pt08"><input type="checkbox" id="chk02" name="mainJob" title="연구 및 공학기술 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'02');" value="02"><label for="chk02"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName02" title="연구 및 공학기술에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('02', 'mainJob10' , 'subJob');">연구 및 공학기술</button><input type="hidden" id="mainJob10Nm" value="연구 및 공학기술"><input type="hidden" name="firstJobName" id="jobName02" value="연구 및 공학기술"></li><li><span class="pt08"><input type="checkbox" id="chk07" name="mainJob" title="영업·판매·운전·운송 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'07');" value="07"><label for="chk07"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName07" title="영업·판매·운전·운송에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('07', 'mainJob11' , 'subJob');">영업·판매·운전·운송</button><input type="hidden" id="mainJob11Nm" value="영업·판매·운전·운송"><input type="hidden" name="firstJobName" id="jobName07" value="영업·판매·운전·운송"></li><li><span class="pt08"><input type="checkbox" id="chk05" name="mainJob" title="예술·디자인·방송·스포츠 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'05');" value="05"><label for="chk05"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName05" title="예술·디자인·방송·스포츠에 속하는 2차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('05', 'mainJob12' , 'subJob');">예술·디자인·방송·스포츠</button><input type="hidden" id="mainJob12Nm" value="예술·디자인·방송·스포츠"><input type="hidden" name="firstJobName" id="jobName05" value="예술·디자인·방송·스포츠"></li></ul>
            </div>
        </div>
        <div class="col">
            <p class="tit">2차 분류</p>
            <div class="cont_area scroll h280">
                <ul class="box_chk-group chk_row job-search-p" id="subJobDiv"><p class="txt">1차 분류를 선택하세요</p></ul>
            </div>
        </div>
        <div class="col">
            <p class="tit">3차 분류</p>
            <div class="cont_area scroll h280">
                <ul class="box_chk-group chk_row job-search-p" id="thirdJobDiv"><p class="txt">2차 분류를 선택하세요</p></ul>
            </div>
        </div>
    </div>

</div><!-- virw1 -->
<div id="wk-jobs-search-view2" style="display: none">
    <div class="list_chk_area only_cont type_col" style="display: block">
        <div class="cont_area" id="wk-jobs-search-content">
        </div>
    </div>
    <span>&nbsp;</span>
    <div>* 분류 리스트로 검색하려면 [분류별보기] 버튼을 클릭하세요.
        <button type="button" class="btn small type02" onclick="viewChange();">분류별 보기</button>
    </div>
</div>
<!--// 본문 컨텐츠 -->
<!-- 버튼 -->
<a href="#none" class="closed" onclick="fn_show('jobCategory');">
    <span class="blind">팝업 닫기</span>
</a>
<!--// 버튼 -->
</div>

5. From the 1st filter, we select the following check box.
<li><span class="pt08"><input type="checkbox" id="chk02" name="mainJob" title="연구 및 공학기술 선택. 선택시 하단의 검색결과에서 확인 가능함" aria-selected="false" onclick="f_checkJob(this,'02');" value="02"><label for="chk02"><span class="blind">선택</span></label></span><button type="button" class="chk_btn active" id="btnjobName02" title="연구 및 공학기술에 속하는 2차분류 조회" aria-selected="true" onclick="fn_requestJobSubList('02', 'mainJob10' , 'subJob');">연구 및 공학기술</button><input type="hidden" id="mainJob10Nm" value="연구 및 공학기술"><input type="hidden" name="firstJobName" id="jobName02" value="연구 및 공학기술"></li>

6. from the second filter we select: 
<li><span class="pt08"><input type="checkbox" id="chk023" title="컴퓨터시스템 선택. 선택시 하단의 검색결과에서 확인 가능함" name="subJob" onclick="f_checkJob(this,'023');" value="023" "=""><label for="chk023"><span class="blind">선택</span></label></span><button type="button" class="chk_btn" id="btnjobName023" title="컴퓨터시스템에 속하는 3차분류 조회" aria-selected="false" onclick="fn_requestJobSubList('023', 'subJob9' , 'thirdJob');">컴퓨터시스템</button><input type="hidden" id="subJob9Nm" value="컴퓨터시스템"><input type="hidden" name="secondJobName" id="jobName023" value="컴퓨터시스템"></li>

7. then we go to the area filter section: Click: <button type="button" class="btn medium type02" onclick="fn_show('jobCatelocation01', 'jobCatelocation02');"><span>지역별</span></button>
8. We choose the Area of Seoul: `<li id="regionOn_11000"><button type="button" onclick="fn_requestRegionSubList('11000');">서울</button></li>`
9. Then we scroll down to click on the search button: <button type="button" onclick="fn_Search('1');" class="btn large type01 fill wd180px"><span>검색</span></button>
10. then we wait for 5 seconds.
