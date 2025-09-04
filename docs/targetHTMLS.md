work24 site url: https://www.work24.go.kr/cm/z/b/0210/openLginPageForAnyId.do?endPoint=%2Fcm%2Fmain.do&acrValues=3&tx=20250902112318764_5000000291_4cca285b-c66c-43ab-9dc1-e9515a831add#/

Login button: 
<a href="javascript:void(0);" id="btnIdPopup" class="link-id full_open" open-full-pop="pop_cert_id" aria-haspopup="dialog">
    <dl class="cert_list">
        <dt>
            <strong class="tit">아이디/비밀번호</strong>
        </dt>
        <dd>
            <div class="cert_info">
                <p class="s1_r"><span class="point_color">고용24 민원신청 시 추가 본인 인증이 필요</span>하며, 아이디/비밀번호 로그인은 직업훈련 출석 확인 등 모바일에서만 사용 가능해요.</p>
            </div>
        </dd>
    </dl>
</a>

ID input field:
<div class="list_txt">
    <div class="box_table_group">
        <div class="cell"> <!-- D: error 일경우 class[error] add -->
            <span class="box_ipt">
                <input type="text" class="input_txt big valid" id="id" name="id" maxlength="30" placeholder="개인회원 ID" title="아이디를 입력해 주세요" aria-invalid="false">
                <button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
            </span>
        </div>
    </div>
</div>

Password input field:
<div class="list_txt ">
    <div class="box_table_group">
        <div class="cell"> <!-- D: error 일경우 class[error] add -->
            <div class="cell_wrap">
                <span class="box_ipt">
                    <input type="password" class="input_txt big valid" id="pwd" name="pwd" maxlength="24" placeholder="개인회원 비밀번호" title="비밀번호를 입력해 주세요" data-enc="on" data-tk-kbdtype="qwerty" aria-invalid="false">
                    <button type="reset" class="ico16_delete"><span class="blind">삭제</span></button>
                </span>
                <!-- <button type="button" class="ico24_keypad h56"><span class="blind">보안키패드</span></button> -->
                <!-- 가상키보드 추가 -->
                <span style="margin-left:5px" id="pwd_tk_btn" data-tk-btntype="img"><button type="button" style="border: none; background: none; padding: 0 0 0 0;" id="Tk_pwd_checkbox" name="Tk_pwd_checkbox"><img alt="가상키보드실행버튼" src="/cm/static/solution/transkey/images/off.png" style="cursor: not-allowed; pointer-events:none; vertical-align:middle;"></button></span>
            </div>
        </div>
    </div>
</div>


After login success, Job list search page: https://www.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do

Job search section:
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
						<div id="jobCategory" style="display:none;" class="layer_section">
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
							<div id="jobCatelocation01" style="display:none " class="layer_section">
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
		<div class="floating_search_result ty2 mt16" style="z-index: 1;">
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
					<span class="tit ml08">검색건수 <span class="txt_total">123,088</span>건</span>
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo0" value="KJKX002509020007|VALIDATION|마음드림재가복지센터|[동백 중동/4등급/독거할머님]  요양보호사 채용" title="마음드림재가복지센터 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('4728001114');">
															마음드림재가복지센터
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KJKX002509020007&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														[동백 중동/4등급/독거할머님]  요양보호사 채용
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KJKX002509020007', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KJKX002509020007', 'tb_workinfoworknet', 'VAL'); return false;">
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
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
												
													신입
												
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
											
											
											<span class="item sm 3">주 9시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												09:00 ~ 12:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경기도 용인시 기흥구 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo0">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
									var closeTpNm = '';
									var wantedYn = 'Y';
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
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo1" value="K131522509020007|VALIDATION|유로스카이어린이집|야간연장반보육교사 모집[거제고용센터 채용대행]" title="유로스카이어린이집 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('8258200706');">
															유로스카이어린이집
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K131522509020007&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														야간연장반보육교사 모집[거제고용센터 채용대행]
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K131522509020007', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K131522509020007', 'tb_workinfoworknet', 'VAL'); return false;">
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
														
														
														
														
															~
															
																
																	
																	
																		
																			350
																		
																		
																	
																
																
															
															만원
														
													
													
													
												
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
											
											
											<span class="item sm 4">
												
												
												14:30 ~ 21:30
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경상남도 거제시 고현항2로 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo1">D-10</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-09-12';
									var closeDt = '25/09/12';
									var closeTpNm = '';
									var wantedYn = 'N';
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
							
							<p class="s1_r">마감일 : 2025-09-12</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo2" value="K150122509020019|VALIDATION|주식회사 대원푸드시스템 농업회사법인|HACCP 인증 업체에서 닭 양념육 제조 및 가공 생산자를 채용합니다." title="주식회사 대원푸드시스템 농업회사법인 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('2268601717');">
															주식회사 대원푸드시스템 농업회사법인
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K150122509020019&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
														HACCP 인증 업체에서 닭 양념육 제조 및 가공 생산자를 채용합니...
													
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K150122509020019', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K150122509020019', 'tb_workinfoworknet', 'VAL'); return false;">
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
												
													
														
															
																연봉
															
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		2,760
																	
																	
																
															
															
														
														만원
														
														
														
														
															~
															
																
																	
																	
																		
																			2,800
																		
																		
																	
																
																
															
															만원
														
													
													
													
												
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
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 40시간 근로</span>
											
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														인천광역시 서구 건지로97번길 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo2">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-10-31';
									var closeDt = '25/10/31';
									var closeTpNm = '';
									var wantedYn = 'Y';
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
							
							<p class="s1_r">마감일 : 2025-10-31</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo3" value="KJ22202509020003|VALIDATION|주식회사 우리원|주식회사 우리원- 생산라인업무" title="주식회사 우리원 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('6038193267');">
															주식회사 우리원
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KJ22202509020003&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														주식회사 우리원- 생산라인업무
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KJ22202509020003', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KJ22202509020003', 'tb_workinfoworknet', 'VAL'); return false;">
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
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		240
																	
																	
																
															
															
														
														만원
														
														
														
														
															~
															
																
																	
																	
																		
																			240
																		
																		
																	
																
																
															
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
												
												
												09:00 ~ 20:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경상북도 칠곡군 동명면 
													
													
												
											
										
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
									var date  = '2025-10-01';
									var closeDt = '25/10/01';
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
							
							<p class="s1_r">마감일 : 2025-10-01</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo4" value="K160042509020021|VALIDATION|주식회사 백건스틸|철강 현장직(상하차·절단) 직원 채용" title="주식회사 백건스틸 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('6988700109');">
															주식회사 백건스틸
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K160042509020021&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														철강 현장직(상하차·절단) 직원 채용
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K160042509020021', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K160042509020021', 'tb_workinfoworknet', 'VAL'); return false;">
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
														
														
														
														
															~
															
																
																	
																	
																		
																			300
																		
																		
																	
																
																
															
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
											
											
											<span class="item sm 4">
												
												
												08:30 ~ 17:30
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														광주광역시 광산구 진곡산단6번로 
													
													
												
											
										
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo5" value="K161222509020004|VALIDATION|（유）신정건설|경리 및 공무" title="（유）신정건설 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('4038156847');">
															（유）신정건설
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K161222509020004&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														경리 및 공무
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K161222509020004', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K161222509020004', 'tb_workinfoworknet', 'VAL'); return false;">
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
														
														이상
														
														
													
													
													
												
											</span>
											
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
													
														
													
												
												
													경력2년
												
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
												
												
												08:00 ~ 17:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														전북특별자치도 김제시 효자로 
													
													
												
											
										
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
									var date  = '2025-10-31';
									var closeDt = '25/10/31';
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
							
							<p class="s1_r">마감일 : 2025-10-31</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo6" value="KF11192509020005|VALIDATION|엔케어재가복지센터|사회복지사 채용합니다." title="엔케어재가복지센터 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('6518002749');">
															엔케어재가복지센터
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KF11192509020005&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														사회복지사 채용합니다.
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KF11192509020005', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KF11192509020005', 'tb_workinfoworknet', 'VAL'); return false;">
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
										
										
											
											
											
											
												
													
														
														전북특별자치도 전주시 완산구 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo6">채용시까지</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-09-16';
									var closeDt = '25/09/16';
									var closeTpNm = '';
									var wantedYn = 'Y';
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
							
							<p class="s1_r">마감일 : 2025-09-16</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo7" value="K161322509020009|VALIDATION|유한회사홍익종합관리|나운세경아파트 전기과장(관리과장) 모집" title="유한회사홍익종합관리 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('4018108581');">
															유한회사홍익종합관리
														</a>
													
												
												<span class="label_box ml08">
													
													<span class="tbl_label brown">중견</span>
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K161322509020009&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														나운세경아파트 전기과장(관리과장) 모집
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K161322509020009', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K161322509020009', 'tb_workinfoworknet', 'VAL'); return false;">
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
															
															
															
														
														
														
														
															
														
														
														
															
																
																
																
																
																	
																		340
																	
																	
																
															
															
														
														만원
														
														이상
														
														
													
													
													
												
											</span>
											
												
													<span class="item b1_sb">상여별도&nbsp;50%</span>
												
											
										</p>

									</li>
									
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											
											<span class="item sm">
												
												
												
													
												
												
													경력
												
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
										
										
											
											
											
											
												
													
														
														전북특별자치도 군산시 하나운로 
													
													
												
											
										
										</p>
									</li>
									
								</ul>
							</div>
						</td>
						<td class="pd24">
							<strong class="t3_sb clr_red" id="dDayInfo7">D-14</strong>
							<script type="text/javascript">
								$(document).ready(function(){
									/**** D-day 구하기 ****/
									var date  = '2025-09-16';
									var closeDt = '25/09/16';
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
							
							<p class="s1_r">마감일 : 2025-09-16</p>
							
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo8" value="KF11702509020002|VALIDATION|행복한노인복지센터|재가요양보호사 구인" title="행복한노인복지센터 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('1388275665');">
															행복한노인복지센터
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KF11702509020002&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														재가요양보호사 구인
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('KF11702509020002', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('KF11702509020002', 'tb_workinfoworknet', 'VAL'); return false;">
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
															
														
														
														
														
														
														
															
															
																12,700
															
														
														원
														
														
														
														
															~
															
																
																
																	12,700
																
															
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
												
													주5일
													
													
													
													
													
													
													
													
													
												
											</span>
											
											
											<span class="item sm 3">주 20시간 근로</span>
											
											
											<span class="item sm 4">
												
												
												15:00 ~ 19:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														경기도 양주시 남면 
													
													
												
											
										
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
												
													<input class="vtalm3" type="checkbox" id="chkboxWantedAuthNo9" value="K162122509020020|VALIDATION|유한회사남해테크|[전남]_(유)남해테크  생산직원(취부 및 용접, 사상공) 모집" title="유한회사남해테크 선택 후 채용정보 비교검색">
												
												
													
													
														<a href="#none" class="cp_name underline_hover" onclick="fnOpenPopup('8568702057');">
															유한회사남해테크
														</a>
													
												
												<span class="label_box ml08">
													
													
												</span>

											</span>
										</label>
									</div>
								</div>
								
									
									<div class="cell">
										
											<a href="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=K162122509020020&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" title="새창 열림" class="t3_sb underline_hover" target="_new" onclick="addEmpInfoHistCookie(this);">
												
													
													
														[전남]_(유)남해테크  생산직원(취부 및 용접, 사상공) 모집
													
												
											</a>
										
										
									</div>
									
									
								
								<div class="cell">
									<p class="vline_group bar_r type2 flex_box flex_wrap">
										<span class="item sm logo_wrap">
											
												
													<img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"> <!-- 241118 alt값 수정 가이드 13번 항목 -->
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
												
											
										</span>

										
										<strong class="item sm clr_blue">고용24 입사지원 가능</strong>
										
										<span class="item sm gap_box04">
											<button title="관심정보 등록" class="icon_btn" onclick="fnBookMarkAdd('K162122509020020', 'VALIDATION', this);return false;">
												<i class="flx-Shk0 ico16_unlike"></i>
											</button>
											<button title="요약보기" class="icon_btn" onclick="fn_showSplLayer('K162122509020020', 'tb_workinfoworknet', 'VAL'); return false;">
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
											
											
											
											<span class="item sm 4">
												
												
												08:00 ~ 17:00
											</span>
											
										</p>
									</li>
									

									
									<li class="site">
										<p>
										
										
											
											
											
											
												
													
														
														전라남도 영암군 삼호읍 
													
													
												
											
										
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
									var date  = '2025-11-01';
									var closeDt = '25/11/01';
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
							
							<p class="s1_r">마감일 : 2025-11-01</p>
							
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
					<div class="set_pagination"><div class="box_pagination"><button type="button" class="btn_page first" onclick="fn_Move(1); return false;"><span class="blind">처음으로 가기</span></button>&nbsp;<button type="button" class="btn_page prev" onclick="fn_Move(1); return false;"><span class="blind">이전</span></button>&nbsp;<button type="button" class="active" title="1 페이지 이동" aria-current="true">1</button>  &nbsp;<button type="button" onclick="fn_Move(2); return false;" title="2 페이지 이동">2</button>&nbsp;<button type="button" onclick="fn_Move(3); return false;" title="3 페이지 이동">3</button>&nbsp;<button type="button" onclick="fn_Move(4); return false;" title="4 페이지 이동">4</button>&nbsp;<button type="button" onclick="fn_Move(5); return false;" title="5 페이지 이동">5</button>&nbsp;<button type="button" onclick="fn_Move(6); return false;" title="6 페이지 이동">6</button>&nbsp;<button type="button" onclick="fn_Move(7); return false;" title="7 페이지 이동">7</button>&nbsp;<button type="button" onclick="fn_Move(8); return false;" title="8 페이지 이동">8</button>&nbsp;<button type="button" onclick="fn_Move(9); return false;" title="9 페이지 이동">9</button>&nbsp;<button type="button" onclick="fn_Move(10); return false;" title="10 페이지 이동">10</button>&nbsp;<button type="button" class="btn_page next" onclick="fn_Move(11); return false;"><span class="blind">다음</span></button>&nbsp;<button type="button" class="btn_page last" onclick="fn_Move(12309); return false;"><span class="blind">마지막으로 가기</span></button>&nbsp;</div></div>
					
				</div>
			</div>
			<!-- //pagination -->
		</div>
	</div>
</form></div>


Job detail page:
<div class="left">
			<div class="sub_tl js_s">
				<h2 class="h2_sb">채용정보 상세</h2>
				<p>
					<a href="#none" class="btn small type02 ml04" onclick="WkEmpInfo.f_copyMenuUrl(); return false;"><i class="ico16_link"></i>링크 복사</a>
					<a href="#none" class="btn small type02 ml04" onclick="f_sndMailEmpInfoPop(); return false;"><i class="ico16_email"></i>이메일 전송</a>
					<a href="#none" class="btn small type02 ml04" onclick="f_empInfoRdPrint(); return false;"><i class="ico_print_guide2 ico16"></i>인쇄하기</a>
				</p>
			</div>
			<div class="tab_wrap bg_type mb40">
				<ul class="tab_title" role="tablist">
					<!-- D: 선택된 탭 button에 aria-selected="true"추가(title="선택됨" 으로 대체 가능) -->
					<li class="active"><button type="button" id="" data-role="tab" aria-selected="true"><span>채용정보</span></button></li>
					
					
				</ul>
				<form id="moveForm" name="moveForm" action="/wk/a/b/1500/empDetailAuthView.do?wantedAuthNo=KJKX002509020007&amp;infoTypeCd=VALIDATION&amp;infoTypeGroup=tb_workinfoworknet" method="post">
					<input type="hidden" id="busiNo" name="busiNo" value="">
					<input type="hidden" id="expCntnClcd" name="expCntnClcd" value="">
					<input type="hidden" id="seqno" name="seqno" value="">
					<input type="hidden" id="wantedAuthNo" name="wantedAuthNo" value="KJKX002509020007">
					<input type="hidden" id="infoTypeGroup" name="infoTypeGroup" value="">
					<input type="hidden" id="infoTypeCd" name="infoTypeCd" value="">

					<input type="hidden" id="strWkHost" name="strWkHost" value="https://www.work.go.kr">
					<input type="hidden" id="strHrdHost" name="strHrdHost" value="https://hrd.work24.go.kr">
				</form>
			</div>

			<!-- 채용정보 -->
			<div class="emp_sumup_wrp">
				<div class="tit_area">
					<div>
						<p class="corp_info">
							<strong>마음드림재가복지센터</strong>
							
							
							
						</p>
						<strong class="title">[동백 중동/4등급/독거할머님]  요양보호사 채용</strong>
					</div>
					<div class="etc_info">
						<p class="flex_box">
							
								
								
									<img src="/wk/static/images/logo/work24.png" alt="고용24">
								
							
							<span class="count">조회수 <strong>0</strong></span>
						</p>
						<p class="flex_box label">
							
							<span class="btn mw_auto small type06 r30 ddayDisplay">채용시까지</span>
						</p>
					</div>
				</div>

				<div class="emp_detail">
					<div class="column">
						<strong class="b1_sb">지원자격</strong>
						<ul class="list">
							<li>
								<em class="tit">경력</em>
								
								
								<p>
									신입
									
									
									
								</p>
							</li>
							<li>
								<em class="tit">학력</em>
								
								
									
									
										
									
									
								
								<p>
									학력무관
								</p>
							</li>
						</ul>
					</div>
					<div class="column">
						<strong class="b1_sb">근무조건</strong>
						<ul class="list">
							<li>
								<em class="tit">임금</em>
								
								
								
								
									
									
										
									
								
								
									
								
								
								<p>
									시급 10,030원 이상 
								</p>
							</li>
							<li>
								<em class="tit">지역</em>
								
								
									
									
										
										
										
											
										
										
										
											
										
									
								
								<p>
									경기도   용인시  기흥구 동백죽전대로 333, 207 (중동, 스프링카운티자이)
									
								</p>
							</li>
						</ul>
					</div>
					<div class="column">
						<strong class="b1_sb">고용형태</strong>
						<ul class="list">
							<li>
								<em class="tit">고용형태</em>
								<p>
									기간의 정함이 없는 근로계약(시간(선택)제)
								</p>
							</li>
							<li>
								<em class="tit">근무형태</em>
								
								
									
									
								
								<p>
									주 3일 근무
									
									
										(주 소정근로시간: 9시간)
									
									
								</p>
							</li>
						</ul>
					</div>
					<div class="column">
						<strong class="b1_sb">복리후생</strong>
						
						<div class="items">
							
							
							
							
							
							
							
							
							
						</div>
					</div>
				</div>
			</div>
			<div class="box_btn_wrap flex_al_c">
				<button type="button" class="btn big type02" id="empBookmkButton" onclick="f_addInterestEmpInfo(this)">
					<i class="ico24_ui_like"></i>관심정보 등록
					
				<em class="blind">해제됨</em></button><!-- D: 선택됐을 경우 class="active", em class="blind" 영역 추가 -->
				
					
						<a href="#" class="btn big type01 fill" onclick="f_resumePop(); return false;">고용24 입사지원</a>
					
					
				
			</div>
			
				<p class="s1_r text_center mt16">고용24 입사지원 클릭 시 응답이 없을 경우, <strong class="clr_blue">강력 새로고침(Ctrl + F5)</strong> 후 다시 시도해보시기 바랍니다.</p>
			

			<div class="tab_wrap line_type mt40">
				<div class="tab_fiexd_wrap newScrollTab"><!-- 탭 fix될 경우 class="fixed" 추가 class="tab_fiexd_wrap fix" -->
					<ul class="tab_title mb40" role="tablist">
						<!-- D: 선택된 버튼에 aria-selected="true" -->
						<li class="tab_list active"><a href="#tab-panel01" aria-controls="tab-panel01" aria-selected="true"><span>모집요강</span></a></li>
						<li class="tab_list"><a href="#tab-panel02" aria-controls="tab-panel02" aria-selected="false"><span>근무조건</span></a></li>
						<li class="tab_list"><a href="#tab-panel03" aria-controls="tab-panel03" aria-selected="false"><span>우대사항</span></a></li>
						<li class="tab_list"><a href="#tab-panel04" aria-controls="tab-panel04" aria-selected="false"><span>복리후생</span></a></li>
						<li class="tab_list"><a href="#tab-panel05" aria-controls="tab-panel05" aria-selected="false"><span>전형방법</span></a></li>
						<li class="tab_list"><a href="#tab-panel06" aria-controls="tab-panel06" aria-selected="false"><span>기업정보</span></a></li>
						<li class="tab_list"><a href="#tab-panel07" aria-controls="tab-panel07" aria-selected="false"><span>추천정보</span></a></li>
					</ul>
				</div>
				<!-- 모집요강 -->
				<div id="tab-panel01" class="scroll">
					<strong class="block t2_sb mb08">모집요강</strong>
					<div class="box_border_type expand mt16">
						
						
							
						
						<div class="fold h240">
							<strong class="block b1_sb mb08">직무내용</strong>
							-&nbsp;동백&nbsp;중동&nbsp;4등급&nbsp;독거할머님&nbsp;재가대상자케어<br>-&nbsp;간병일상생활지원서비스(말벗,&nbsp;일상생활지원)<br>-&nbsp;주3일&nbsp;:&nbsp;09:00~12:00(시간협의)<br>-&nbsp;급여&nbsp;:&nbsp;시급10,030&nbsp;+&nbsp;수당&nbsp;등=12,800원<br>-&nbsp;지원문의&nbsp;010-4598-4832<br><br>※근로계약기간의&nbsp;정함이&nbsp;없는&nbsp;근로자를&nbsp;채용하는&nbsp;것이라&nbsp;하더라도&nbsp;실제&nbsp;서비스&nbsp;제공기간에&nbsp;따라&nbsp;임금을&nbsp;계산하여&nbsp;지급하는&nbsp;형태로&nbsp;채용&nbsp;시&nbsp;근로자마다&nbsp;주&nbsp;소정근로시간이나&nbsp;임금,&nbsp;근무(예정)지&nbsp;등에&nbsp;차이가&nbsp;있을&nbsp;수&nbsp;있습니다.
						</div>
						<button type="button" class="btn_toggle_more" style="" aria-expanded="false">더보기<i></i></button>
						<button type="button" class="btn_toggle_more on" style="display: none;">접기<i></i></button>
					</div>

					<div class="box_table_wrap write mt16">
						<table class="box_table"><caption>모집 인원,장애인 채용 인원,모집 직종,관련 직종,직종 키워드,경력,학력,자격 면허을(를) 제공하는 표</caption>
							
							<colgroup>
								<col style="width:19%">
								<col>
								<col style="width:19%">
								<col>
							</colgroup>
							<tbody>
								<tr>
									<th scope="row">모집 인원</th>
									<td>
										1명
									</td>
									<th scope="row">장애인 채용 인원</th>
									
									
										
										
									
									<td>
										
											
											-
										
										
									</td>
								</tr>
								<tr>
									<th scope="row">모집 직종</th>
									<td>
										요양보호사
									</td>
									<th scope="row">관련 직종</th>
									
									
										
											
											
										
										
									
									<td>
										재가 요양보호사
									</td>
								</tr>
								<tr>
									<th scope="row">직종 키워드</th>
									<td colspan="3">
										
											
											-
										
									</td>
								</tr>
								<tr>
									<th scope="row">경력</th>
									<td>
										신입
										
										
										
									</td>
									<th scope="row">학력</th>
									<td>
										학력무관
									</td>
								</tr>
								<tr>
									<th scope="row">자격 면허</th>
									
									
									
									
									
										
										
											
										
									
									
									<td colspan="3">
										
										
											
												
													
													
													
														
															
															
														
														
													
													<p>
														<span class="tbl_label fill f_weight_400 sky">필수</span>
														요양보호사
													</p>
													
												
												
												
											
											
										
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<!-- //모집요강 -->
				<!-- 근무조건 -->
				<div id="tab-panel02" class="mt70 scroll">
					<strong class="block t2_sb mb08">근무조건</strong>
					<div class="box_table_wrap write mt16"><!-- 20241023 class 수정 -->
						<table class="box_table"><caption>고용 형태,임금 조건,근무 시간,휴게 시간,근무 형태,사회보험,퇴직급여,근무 예정지,인근 전철역,버스 노선 번호을(를) 제공하는 표</caption>
							
							<colgroup>
								<col style="width:19%">
								<col>
								<col style="width:19%">
								<col>
							</colgroup>
							<tbody>
								<tr>
									<th scope="row">고용 형태</th>
									<td>
										기간의 정함이 없는 근로계약(시간(선택)제)
										
										
										
									</td>
									<th scope="row">임금 조건</th>
									
									
									<td>
										시급 10,030원 이상 
										
										
										
									</td>
								</tr>
								<tr>
									<th scope="row">근무 시간</th>
									<td colspan="3">
										
											<strong>
												<strong>
													주 소정근로시간
													<div class="box_tooltip type2">
														<button type="button" class="btn_help dis"><span class="blind">도움말</span></button><!-- 20241023 class 수정 -->
														<div class="box_help-data w_big">
															<p class="s1_r lh24">※ "주소정근로시간" 이란<br>근로자와 사용자가 정한 1주 동안 근로하는 근로시간을 말합니다.</p>
															<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
															</button>
														</div>
													</div>: 9시간
											</strong>
											<br><br>
										

										
											
											
												
													
													
														<strong>상세 근무시간</strong>
													<p>
															(근무시간)&nbsp;(오전)&nbsp;9시&nbsp;00분&nbsp;~&nbsp;(정오)&nbsp;12시&nbsp;00분
														</p>
													
													
												
											
										
										
											<p><span class="tbl_label fill sky mr04">근무시간 협의가능</span></p>
											<br>
										

										
										
										
											
											
												<br>
											
										


										
										

									</strong></td>

								</tr>
								<tr>
									<th scope="row">휴게 시간</th>
									<td>
										
											-
											
										
									</td>
									<th scope="row">근무 형태</th>
									<td>
										
											주 3일 근무
										
									</td>
								</tr>
								<tr>
									<th scope="row">사회보험</th>
									
									
									
									
										
										
									
									
										
										
									
									
									<td>
										
											 고용보험, 산재보험
											
										
									</td>
									<th scope="row">퇴직급여</th>
									<td>
										퇴직금
									</td>
								</tr>
								<tr>
									<th scope="row">근무 예정지</th>
									<td colspan="3">
										<div class="flex_box js_s">
											<p>
												
												
												
													
													
														<!-- 도로명 주소 -->
														
														
															
																
																	
																
																
															
														
														
															
														
													
												
												경기도 용인시 기흥구 동백죽전대로 333, 207 (중동, 스프링카운티자이)
											</p>
											<div id="daumLocalScript"></div>
											<button type="button" class="btn small tbl_type02 btn_fold" title="지도보기 펼치기" data-addr="경기도 용인시 기흥구 동백죽전대로 333, 207 (중동, 스프링카운티자이)" data-map-coor-x="" data-map-coor-y="" onclick="f_showWorkLocationMap(this.dataset.addr, this.dataset.mapCoorX, this.dataset.mapCoorY, this);">지도 보기</button>
										</div>
										<!-- 지도영역 -->
										<div id="map_wrap" class="mt08" style="display:none;">
											<div class="map" id="workLocationMap" style="position: relative; overflow: hidden; background: url(&quot;https://t1.daumcdn.net/mapjsapi/images/bg_tile.png&quot;);"></div>
											<button type="button" class="btn small type02 ico_type" onclick="f_getDirections();" title="새창 열림">길찾기</button>
										</div>
										<!-- //지도영역 -->
									</td>
								</tr>
								<tr>
									<th scope="row">인근 전철역</th>
									<td colspan="3">
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">버스 노선 번호</th>
									<td colspan="3">
										
											-
											
										
									</td>
								</tr>
							</tbody>
						</table>
					</div>
					<ul class="box_list_area f_14 mt08">
						<li class="txt_list">『고용상 연령차별금지 및 고령자 고용촉진에 관한 법률』 이 시행됨에 따라 채용정보에서 연령이 삭제되었습니다.</li>
					</ul>
				</div>
				<!-- //근무조건 -->

				<!-- 우대사항 -->
				<div id="tab-panel03" class="mt70 scroll">
					<strong class="block t2_sb mb08">우대사항</strong>
					<div class="box_table_wrap write mt16"><!-- 20241023 class 수정 -->
						<table class="box_table"><caption>전공,컴퓨터 활용 능력,외국어 능력,우대조건,기타 우대사항을(를) 제공하는 표</caption>
							
							<colgroup>
								<col style="width:19%">
								<col>
							</colgroup>
							<tbody>
								<tr>
									<th scope="row">전공</th>
									
									
									
									

									<td>
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">컴퓨터 활용 능력</th>
									<td>
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">외국어 능력</th>
									<td>
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">우대조건</th>
									
									
									
									
										
										
									
									
									<td>
										
											
											 (준)고령자(50세이상)
										
									</td>
								</tr>
								<tr>
									<th scope="row">기타 우대사항</th>
									<td>
										
											-
											
										
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<!-- //우대사항 -->
				<!-- 기타사항 -->
				<div class="mt70">
					<strong class="block t2_sb mb08">기타사항</strong>
					<div class="box_table_wrap write mt16"><!-- 20241023 class 수정 -->
						<table class="box_table"><caption>고용허가제,병역 대체 복무자 채용을(를) 제공하는 표</caption>
							
							<colgroup>
								<col style="width:19%">
								<col>
							</colgroup>
							<tbody>
								<tr>
									<th scope="row">고용허가제</th>
									<td>
										
											
											-
										
									</td>
								</tr>
								<tr>
									<th scope="row">병역 대체 복무자 채용</th>
									
									
									
									
									
									
									<td>
										
											
											비희망
										
									</td>
								</tr>
							</tbody>
						</table>
					</div>
					<div class="box_border_type mt16">
						<strong class="block b1_sb mb08">그 밖의 희망사항</strong>
						<div class="b1_r">
							
								-
								
							
						</div>
					</div>
				</div>
				<!-- //기타사항 -->
				<!-- 복리후생 -->
				<div id="tab-panel04" class="mt70 scroll">
					<strong class="block t2_sb mb08">복리후생</strong>
					<div class="box_border_type fill mt16"><!-- 20241023 class 수정 -->
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						<ul class="emp_box_items col5">
							<!-- D: 미제공인경우 li class="disable" 추가, p태그 <em class="blind">미제공</em> 추가 -->
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare1.png" alt=""></span>
								<p class="mt08">통근버스<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare2.png" alt=""></span>
								<p class="mt08">기숙사<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare3.png" alt=""></span>
								<p class="mt08">차량유지비<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare4.png" alt=""></span>
								<p class="mt08">교육비 지원<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare5.png" alt=""></span>
								<p class="mt08">자녀 학자금 지원<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare6.png" alt=""></span>
								<p class="mt08">주택자금 지원<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare7.png" alt=""></span>
								<p class="mt08">직원대출제도<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare8.png" alt=""></span>
								<p class="mt08">모성보호시설<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<span class="img_wrp"><img src="/wk/static/images/welfare9.png" alt=""></span>
								<p class="mt08">식사제공<em class="blind">미제공</em></p>
							</li>
						</ul>
					</div>

					<div class="box_border_type mt16">
						<strong class="block b1_sb mb08">기타 복리후생</strong>
						<p class="b1_r">
							
								
								-
							
						</p>
					</div>

					<div class="mt70">
						<strong class="block t2_sb mb08">장애인용 복지시설</strong>
						<div class="box_border_type fill mt16"><!-- 20241023 class 수정 -->
							
							
							
							
							
							
							
							
							
							<ul class="emp_box_items">
								<li class="disable">
									<span class="img_wrp"><img src="/wk/static/images/welfare10.png" alt=""></span>
									<p class="mt08">장애인용 주차장<em class="blind">미제공</em></p>
								</li>
								<li class="disable">
									<span class="img_wrp"><img src="/wk/static/images/welfare11.png" alt=""></span>
									<p class="mt08">장애인용 승강기<em class="blind">미제공</em></p>
								</li>
								<li class="disable">
									<span class="img_wrp"><img src="/wk/static/images/welfare12.png" alt=""></span>
									<p class="mt08">장애인용 화장실<em class="blind">미제공</em></p>
								</li>
								<li class="disable">
									<span class="img_wrp"><img src="/wk/static/images/welfare13.png" alt=""></span>
									<p>건물 내부 경사로<em class="blind">미제공</em></p>
								</li>
							</ul>
						</div>
						<div class="box_border_type mt16">
							<strong class="block b1_sb mb08">기타 장애인용 복지시설</strong>
							<p class="b1_r">
								
									
									-
								
							</p>
						</div>
					</div>
				</div>
				<!-- //복리후생 -->
				<!-- 작업환경 -->
				<div class="mt70">
					<strong class="block t2_sb mb08">작업환경</strong>
					<div class="box_table_wrap write mt16"><!-- 20241023 class 수정 -->
						<table class="box_table"><caption>작업 장소,드는 힘,서거나 걷기,듣고 말하기,시력,손 작업,양손 작업을(를) 제공하는 표</caption>
							
							<colgroup>
								<col style="width:19%">
								<col>
								<col style="width:19%">
								<col>
							</colgroup>
							<tbody>
								<tr>
									<th scope="row">작업 장소</th>
									<td colspan="3">
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">드는 힘</th>
									<td>
										
											-
											
										
									</td>
									<th scope="row">서거나 걷기</th>
									<td>
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">듣고 말하기</th>
									<td>
										
											-
											
										
									</td>
									<th scope="row">시력</th>
									<td>
										
											-
											
										
									</td>
								</tr>
								<tr>
									<th scope="row">손 작업</th>
									<td>
										
											-
											
										
									</td>
									<th scope="row">양손 작업</th>
									<td>
										
											-
											
										
									</td>
									<!-- D: td 컨텐츠 없을 경우 - 처리 -->
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<!-- //작업환경 -->
				<!-- 전형방법 -->
				<div id="tab-panel05" class="mt70 scroll">
					<strong class="block t2_sb mb08">전형방법</strong>
					<!-- 20241023 수정 -->
					<div class="box_border_type fill mt16">
						
						
						
						
							
						
						
						
							
						
						
						
						
						
						<ul class="emp_box_items line">
							<li>
								<p><img src="/wk/static/images/ico16_article.png" class="mr08" alt="">서류</p>
							</li>
							<li>
								<p><img src="/wk/static/images/ico16_member_gray.png" class="mr08" alt="">면접</p>
							</li>
							<li class="disable">
								<p><img src="/wk/static/images/ico16_member_register.png" class="mr08" alt="">필기<em class="blind">미제공</em></p>
							</li>
							<li class="disable">
								<p><img src="/wk/static/images/ico16_faq.png" class="mr08" alt="">기타<em class="blind">미제공</em></p>
							</li>
						</ul>
					</div>
					<!-- //20241023 수정 -->
					
					<div class="box_border_type mt16">
						<div class="emp_colbox_div">
							<div class="left_area br js_s">
								<div>
									<strong class="block b1_sb mb08">접수 마감일</strong>
									
										
											<p class="b1_sb cl-red mb08">
												채용시까지
												(마감시간 : 24시)
											</p>
										
										
									
								</div>
								<div>
									
										<a href="#none" class="btn large fill type01 wd100per mt08" onclick="f_resumePop(); return false;">고용24 입사지원</a>
									
									
								</div>
							</div>
							<div class="flex1">
								<strong class="block b1_sb mb08">접수 방법</strong>
								<!-- D: 텍스트 쓰는대로 보여지는 경우 <div class="b1_r">텍스트</div>로 텍스트 br태그 사용하여 입력-->
								<p class="b1_r">
									고용24,<br>기타&nbsp;(유선&nbsp;통화&nbsp;후&nbsp;지원(010-4598-4832))
								</p>
								<strong class="block b1_sb mt24 mb08">제출 서류</strong>
								<p class="b1_r">
									
									
									
									
									기타(채용&nbsp;확정시&nbsp;건강검진표추가제출)
									
								</p>
								<ul>
									
								</ul>
							</div>
						</div>
					</div>
					<ul class="box_list_area mt08 f_14">
					
						
						<li class="txt_list">
							당사는 자사 이력서, 기초심사자료 등 채용심사 서류에 직무수행과 무관한 구직자의 개인정보*를 포함하지 않습니다. <span class="cl-236DAA">(채용절차의 공정화에 관한 법률 제4조의3)</span><br>
							*구직자 본인의 용모·키·체중·출신지역·혼인여부·재산, 구직자의 직계 존비속 및 형제자매의 학력·직업·재산 등 개인정보 수집 금지
						</li>
						<li class="txt_list">
							당사는 채용 확정 후 <strong>불합격자</strong>가 채용서류의 반환을 청구하면 <strong>14일 이내에 반환</strong>합니다. 이 때 우편발송 요금 등 반환 <strong>소요 비용</strong>은 당사 부담이 원칙입니다. <span class="cl-236DAA">(채용절차의 공정화에 관한 법률 제11조)</span><br>
							*반환청구 기간은 구직자의 채용 여부가 확정된 날 이후 14일부터 180일까지의 기간의 범위에서 당사가 정한 기간으로 함. <span class="cl-236DAA">(채용절차의 공정화에 관한 법률시행령 제4조)</span>
						</li>
						<li class="txt_list">당사는 <strong>채용서류 반환청구 기간이 지난 경우 채용서류를 모두 파기</strong>합니다. <span class="cl-236DAA">(채용절차의 공정화에 관한 법률 제11조)</span></li>
						
						
					
					</ul>
				</div>
				<!-- 전형방법 -->
				<!-- 채용 담당자 -->
				<div class="mt70">
					<strong class="block t2_sb mb08">채용 담당자</strong>
					<div class="box_border_type fill expand mt16"><!-- 20241023 class 수정 -->
						<div class="fold"><!-- D: 확장 시 class="fold on" 추가 -->
							<div class="text_center">
								<p class="f_size_18 cl-red"><i class="ico24_danger_fill vm"></i> <strong>채용 담당자 정보 열람 시 주의사항</strong></p>
								<p class="b1_r mt08 mb08">
									채용 담당자의 개인정보(연락처, 이메일)는 <strong>채용</strong> 및 <strong>취업</strong>을 위해서 제공된 정보입니다.<br>
									이외의 목적으로 사용시 <strong class="cl-red">징역·벌금</strong>에 처할 수 있습니다.
								</p>
								<a href="javascript:void(0)" class="btn large type02" onclick="WkEmpInfo.fn_personalInformationProtectionActPopup(); return false;">개인정보보호법 상세 보기</a>
							</div>
							<!-- D: ul 영역 default는 display:none; /fold on 됐을 경우 display:block; -->
							<!-- 250626 추가 -->
							<ul class="mt32">
								
									
									
										
											
											
											
												
													
												
												
											
											<li class="box_border_type type_pd24 type01 mt08">
												<div class="line_type"><!-- 이름 숨길 시 class="hide" 추가 하거나 div class="line_type" 영역 날리는 방법 중 택1 -->
													<div class="flex_box js_s">
														<p class="b1_sb">최영애</p>
														
													</div>
												</div>
												<div class="line_type">
													<div class="vline_group bar_r type2 flex_box flex_wrap">
														
															<span class="item fs-16"><span class="cl-555 mr08">전화번호</span>
																031-263-4832
																
															</span>
														
														
															<span class="item fs-16"><span class="cl-555 mr08">팩스</span>031-263-4835</span>
														
														
															
															
																
																	<div class="item">
																		<button type="button" class="btn small type01 fill" data-emp-charger-seq="1" onclick="f_displayEmpChargerInfo(this.dataset.empChargerSeq, this);">채용 담당자 개인정보 보기</button>
																	</div>
																
															
														
													</div>
												</div>
											</li>
										
									
								
							</ul>
							<!-- //250626 추가 -->
						</div>
					</div>
					
					<div class="box_border_type fill mt16">
						<div class="flex_box js_s mb08">
							<p class="b1_sb">채용 담당자에게 질문하기</p>
							<p class="s1_r"><span class="cl-orange">*로그인 후 작성 가능합니다.</span></p>
						</div>
						<iframe style="border:none;width:100%" src="/wk/a/b/1512/empChargerInquiryView.do" title="채용 담당자와의 한마디 프레임"></iframe>
						<ul class="box_list_area f_14 mt08">
							<li class="txt_list">이 댓글에 대한 법적 책임은 작성자에게 귀속됩니다.</li>
							<li class="txt_list">권리침해구제: <span class="cl-red">인터넷피해구제센터 (remedy.kocsc.or.kr)</span></li>
							
						</ul>
					</div>
				</div>
				<!-- //채용 담당자 -->
				<!-- 입사지원 현황 -->
				<div class="mt70">
					<div class="box_table_hd">
						<strong class="block t2_sb">입사지원 현황</strong>
						
					</div>
					<div class="box_border_type fill">
						<ul class="emp_box_items col3">
							<li>
								<p class="b1_sb">총 지원자 수</p>
								<strong class="fs-20 mt08 clr_blue">0명</strong>
							</li>
							<li>
								<div class="b1_sb">
									취업알선기관 알선
									<div class="box_tooltip type2">
										<button type="button" class="btn_help dis"><span class="blind">도움말</span></button><!-- 20241023 class 수정 -->
										<div class="box_help-data w_big">
											<p class="s1_r lh24">관할고용센터(또는 취업알선기관)의 취업알선 서비스를 통해 알선된 알선자수.<br>관할 취업알선기관의 취업알선담당자에게 서비스를 요청하시기 바랍니다.</p>
											<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
											</button>
										</div>
									</div>
								</div>
								<strong class="fs-20 mt08">
									
										
										0명
									
								</strong>
							</li>
							<li>
								<div class="b1_sb">
									고용24 입사지원
									<div class="box_tooltip type2">
										<button type="button" class="btn_help dis"><span class="blind">도움말</span></button><!-- 20241023 class 수정 -->
										<div class="box_help-data w_large">
											<p class="s1_r lh24">고용24 웹사이트를 통해 고용24입사지원한 지원자수.<br>고용24 입사지원 기능을 이용하시기 바랍니다.</p>
											<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
											</button>
										</div>
									</div>
								</div>
								<strong class="fs-20 mt08">
									
										
										
											0명
										
									
								</strong>
							</li>
						</ul>
						<ul class="box_list_area f_14 mt08">
							<li class="txt_list">한 지원자가 알선과 고용24 입사지원을 모두 한 경우, 총 지원자 수에서는 한 명으로 집계 됩니다.</li>
						</ul>
					</div>
					
				</div>
				<!-- //입사지원 현황 -->
				<!-- 인증기관 정보 -->
				<div class="mt70">
					<div class="box_table_hd">
						<strong class="block t2_sb">인증기관 정보</strong>
						
						<a href="/wk/f/e/1000/retrieveLieJobadRptList.do" class="btn small type02"><span class="btn_ico ico_siren bg16">거짓구인광고 신고</span></a>
					</div>
					<div class="box_table_wrap write">
						<table class="box_table"><caption>채용공고 등록일시,
										인증기관
										,인증기관 연락처,
										구인인증번호
										을(를) 제공하는 표</caption>
							
							<colgroup>
								<col style="width:19%">
								<col>
								<col style="width:19%">
								<col>
							</colgroup>
							<tbody>
								<tr>
									<th scope="row">채용공고 등록일시</th>
									<td>
										2025.09.02 11:39:57
									</td>
									<th scope="row">
										인증기관
										<div class="box_tooltip type2">
											<button type="button" class="btn_help dis"><span class="blind">도움말</span></button><!-- 20241023 class 수정 -->
											<div class="box_help-data w_large">
												<p class="s1_r lh24">해당 채용정보를 인증한 기관(고용센터, 민간위탁기관 및 지자체)의 담당자입니다.</p>
												<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
												</button>
											</div>
										</div>
									</th>
									<td>
										<div class="flex_box js_s">
											<p>
												경기도 용인시청
											</p>
											<button type="button" class="btn small ico_type tbl_type02" onclick="f_openAuthOrgMapView('JKX00')">지도 보기</button>
										</div>
									</td>
								</tr>
								<tr>
									<th scope="row">인증기관 연락처</th>
									<td>
										
										031-6193-6844
									</td>
									<th scope="row">
										구인인증번호
										<div class="box_tooltip type2">
											<button type="button" class="btn_help dis"><span class="blind">도움말</span></button><!-- 20241023 class 수정 -->
											<div class="box_help-data w_large">
												<p class="s1_r lh24">
													구인업체의 구인신청건에 대한 고유식별번호입니다.<br>
													예) K13004&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;120514&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0001<br>
													&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(기관코드)&nbsp;&nbsp;&nbsp;(인증일자)&nbsp;&nbsp;&nbsp;(일련번호)
												</p>
												<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
												</button>
											</div>
										</div>
									</th>
									<td>
										KJKX002509020007
									</td>
								</tr>
							</tbody>
						</table>
					</div>
					<ul class="box_list_area f_14 mt08">
						<li class="txt_list">
							채용정보가 사실과 다를 경우, 직업안정법 제45조의 3 및 불법직업소개 등 신고포상금제 운영 규정 제2조에 따라 <span class="cl-red">거짓구인광고 및 불법직업소개행위 신고</span>를 할 수 있습니다.
							(단, 허위로 신고할 경우 형법 제156조의 무고죄로 처벌 될 수 있으니 유의하시기 바랍니다.)
						</li>
						<li class="txt_list">
							채용공고에 대한 문의는 <span class="cl-red">채용 담당자 정보 열람하기</span>의 연락처로 문의해주시기 바랍니다.
						</li>
					</ul>
				</div>
				<!-- //인증기관 정보 -->
				<!-- 기업정보 -->
				<div id="tab-panel06" class="mt70 scroll">
					<div class="box_table_hd">
						<strong class="block t2_sb">기업정보</strong>
						
					</div>
					<div class="box_border_type">
						<div class="emp_colbox_div">
							<div class="left_area br">
								<p class="corp_logo_area">
									
										
											<img src="/wk/static/images/img_logo_none.png" class="corp_logo" alt="로고없음">
										
										
									
								</p>
								<div class="corp_btn_area">
									<button type="button" class="btn small type02 flex1" id="companyBookmkButton" onclick="f_addInterestCompany(this)"><i class="ico16_scrap"></i>관심기업<em class="blind">해제됨</em></button><!-- D: 선택 시 class="active" 추가, <em class="blind">선택됨</em> 추가 -->
									<button type="button" class="btn small type02 flex1" id="companyBlockButton" onclick="f_blockCompany(this)"><i class="ico16_shutoff"></i>열람차단<em class="blind">해제됨</em></button>
								</div>
							</div>
							<div class="flex_box flex_al_s gap40 flex1">
								<ul class="corp_info_grp">
									<li>
										<em class="tit">기업명</em>마음드림재가복지센터
									</li>
									<li>
										<em class="tit">업종</em>방문 복지서비스 제공업
									</li>
									<li>
										<em class="tit">기업규모</em>
										
											-
											
										
									</li>
								</ul>
								<ul class="corp_info_grp">
									<li>
										<em class="tit">설립연도</em>
										
											-
											
										
									</li>
									<li>
										<em class="tit">연매출액</em>
										
											-
											
										
									</li>
									
										<li>
											<em class="tit">근로자수</em>55명
										</li>
									
								</ul>
							</div>
							<div class="r_btn_area wd120px js_start">
								
								<a href="#" class="btn small type02 wd100per" onclick="WkEmpInfo.f_showEmployHistoryInfo(WANTED_CUST_NO); return false;">채용정보 이력</a>
							</div>
						</div>
					</div>
				</div>
				<!-- //기업정보 -->
				<!-- 진행 중인 다른 채용공고 -->
				<div class="mt70" id="currentEmployInfoArea">
					
					
				<div class="box_table_hd">
					<strong class="block t2_sb">
						진행 중인 다른 채용공고
					</strong>
					<div>
			
						<span class="s1_r">등록일 기준 최근 3건만 조회됩니다.</span></div></div><div class="box_border_type mb16 currentEmployInfoElement">
						<div class="emp_colbox_div">
							<div class="left_area br wd380px">
								<p class="b1_r">
							<strong class="cl-red mr08">채용시까지</strong> 
								</p>
								<strong class="txt_ellipsis3 t3_sb clr_333 mt08">
									<a href="/wk/a/b/1500/empDetailAuthView.do?infoTypeGroup=tb_workinfoworknet&amp;wantedAuthNo=KJKX002508220015&amp;infoTypeCd=WORKNET" class="t3_sb underline_hover">[개포동 /4등급/독거할머님]   요양보호사 채용</a>
								</strong>
							</div>
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item sm">1명</span><span class="item sm">경력</span><span class="item sm">학력무관</span>
										</p>
									</li>
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item sm">비정규</span>
											<span class="item sm">주 5일 근무</span>
										</p>
									</li>
									<li class="dollar">
										<p>시급 10,030원이상</p>
									</li>
									<li class="site">
										<p>서울특별시 강남구 개포로</p>
									</li>
								</ul>
							</div>
							<div class="r_btn_area wd120px">
								<span class="logo"><img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"></span><p><a href="javascript:void(0);" class="btn small type02 wd100per empInfoSummary" data-wanted-auth-no="KJKX002508220015">요약보기</a></p>	<p><a href="/wk/a/b/1500/empDetailAuthView.do?infoTypeGroup=tb_workinfoworknet&amp;wantedAuthNo=KJKX002508220015&amp;infoTypeCd=WORKNET" class="btn small type02 wd100per" title="새창 열림" target="_blank">새창보기</a></p>
							</div>
						</div>
					</div><div class="box_border_type mb16 currentEmployInfoElement">
						<div class="emp_colbox_div">
							<div class="left_area br wd380px">
								<p class="b1_r">
							<strong class="cl-red mr08">채용시까지</strong> 
								</p>
								<strong class="txt_ellipsis3 t3_sb clr_333 mt08">
									<a href="/wk/a/b/1500/empDetailAuthView.do?infoTypeGroup=tb_workinfoworknet&amp;wantedAuthNo=KJKX002509010006&amp;infoTypeCd=WORKNET" class="t3_sb underline_hover">[중동/3등급/독거할머님]   요양보호사 채용</a>
								</strong>
							</div>
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item sm">1명</span><span class="item sm">관계없음</span><span class="item sm">학력무관</span>
										</p>
									</li>
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item sm">비정규</span>
											<span class="item sm">주 5일 근무</span>
										</p>
									</li>
									<li class="dollar">
										<p>시급 10,030원이상</p>
									</li>
									<li class="site">
										<p>경기도 용인시 기흥구 동백죽전대로</p>
									</li>
								</ul>
							</div>
							<div class="r_btn_area wd120px">
								<span class="logo"><img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"></span><p><a href="javascript:void(0);" class="btn small type02 wd100per empInfoSummary" data-wanted-auth-no="KJKX002509010006">요약보기</a></p>	<p><a href="/wk/a/b/1500/empDetailAuthView.do?infoTypeGroup=tb_workinfoworknet&amp;wantedAuthNo=KJKX002509010006&amp;infoTypeCd=WORKNET" class="btn small type02 wd100per" title="새창 열림" target="_blank">새창보기</a></p>
							</div>
						</div>
					</div><div class="box_border_type mb16 currentEmployInfoElement">
						<div class="emp_colbox_div">
							<div class="left_area br wd380px">
								<p class="b1_r">
							<strong class="cl-red mr08">채용시까지</strong> 
								</p>
								<strong class="txt_ellipsis3 t3_sb clr_333 mt08">
									<a href="/wk/a/b/1500/empDetailAuthView.do?infoTypeGroup=tb_workinfoworknet&amp;wantedAuthNo=KJKX002508290003&amp;infoTypeCd=WORKNET" class="t3_sb underline_hover">[개포동 /5등급/독거할머님]   요양보호사 채용</a>
								</strong>
							</div>
							<div class="flex1">
								<ul class="emp_info_dtl">
									<li class="member">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item sm">1명</span><span class="item sm">신입</span><span class="item sm">학력무관</span>
										</p>
									</li>
									<li class="time">
										<p class="vline_group bar_r type2 flex_box flex_wrap">
											<span class="item sm">비정규</span>
											<span class="item sm">주 5일 근무</span>
										</p>
									</li>
									<li class="dollar">
										<p>시급 10,030원이상</p>
									</li>
									<li class="site">
										<p>서울특별시 강남구 개포로</p>
									</li>
								</ul>
							</div>
							<div class="r_btn_area wd120px">
								<span class="logo"><img src="/wk/static/images/logo/work24.png" alt="정보제공처 고용24"></span><p><a href="javascript:void(0);" class="btn small type02 wd100per empInfoSummary" data-wanted-auth-no="KJKX002508290003">요약보기</a></p>	<p><a href="/wk/a/b/1500/empDetailAuthView.do?infoTypeGroup=tb_workinfoworknet&amp;wantedAuthNo=KJKX002508290003&amp;infoTypeCd=WORKNET" class="btn small type02 wd100per" title="새창 열림" target="_blank">새창보기</a></p>
							</div>
						</div>
					</div></div>
				<!-- //진행 중인 다른 채용공고 -->
				<!-- 빅데이터 추천 정보 -->
				<div class="mt70 scroll">
					<strong class="t2_sb">빅데이터 추천 정보</strong>
					<div class="box_tooltip type2">
						<button type="button" class="btn_help dis"><span class="blind">도움말</span></button><!-- 20241023 class 수정 -->
						<div class="box_help-data w_big">
							<p class="s1_r">선택하신 채용정보에 포함된 키워드들을 분석하여 진로 탐색에 유용한 훈련 및 자격정보 등을 제공하는 서비스입니다.</p>
							<button type="button" class="ico16_delete tooltip_close"><span class="blind">닫기</span>
							</button>
						</div>
					</div>

					<div class="box_side_wrap mt16" id="empBigDataList">
						
					<div class="box_border_type"><p class="text_center cl-grey">연관된 추천 정보가 없습니다.</p></div></div>

				</div>
				<!-- //빅데이터 추천 정보 -->
			</div>
		</div>





SearchKeyword input section:

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