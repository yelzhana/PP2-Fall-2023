{"payload":{"allShortcutsEnabled":false,"fileTree":{"lab9":{"items":[{"name":"1task.py","path":"lab9/1task.py","contentType":"file"},{"name":"2task.py","path":"lab9/2task.py","contentType":"file"},{"name":"3task.py","path":"lab9/3task.py","contentType":"file"}],"totalCount":3},"":{"items":[{"name":"lab2","path":"lab2","contentType":"directory"},{"name":"lab3","path":"lab3","contentType":"directory"},{"name":"lab4","path":"lab4","contentType":"directory"},{"name":"lab5","path":"lab5","contentType":"directory"},{"name":"lab6","path":"lab6","contentType":"directory"},{"name":"lab7","path":"lab7","contentType":"directory"},{"name":"lab8","path":"lab8","contentType":"directory"},{"name":"lab9","path":"lab9","contentType":"directory"},{"name":"1.py","path":"1.py","contentType":"file"},{"name":"10.py","path":"10.py","contentType":"file"},{"name":"11.py","path":"11.py","contentType":"file"},{"name":"12.py","path":"12.py","contentType":"file"},{"name":"13.py","path":"13.py","contentType":"file"},{"name":"2.py","path":"2.py","contentType":"file"},{"name":"3.py","path":"3.py","contentType":"file"},{"name":"4.py","path":"4.py","contentType":"file"},{"name":"5.py","path":"5.py","contentType":"file"},{"name":"6.py","path":"6.py","contentType":"file"},{"name":"7.py","path":"7.py","contentType":"file"},{"name":"8.py","path":"8.py","contentType":"file"},{"name":"9.py","path":"9.py","contentType":"file"},{"name":"lab1.py","path":"lab1.py","contentType":"file"}],"totalCount":22}},"fileTreeProcessingTime":4.806795,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":688880394,"defaultBranch":"main","name":"PP2-Fall-2023","ownerLogin":"dlllnaz","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-09-08T09:50:07.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/144439710?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1700239599.0","canEdit":false,"refType":"branch","currentOid":"5b8c53b5b7500fdcdf8882991ba9924c69727998"},"path":"lab9/3task.py","currentUser":null,"blob":{"rawLines":["import pygame\r","import sys\r","pygame.init()\r","width, height = 800, 600\r","screen = pygame.display.set_mode((width, height))\r","pygame.display.set_caption(\"Moving Ball\")\r","\r","ball_radius = 25\r","ball_color = (255, 0, 0)  # Red\r","ball_pos = [width // 2, height // 2]  \r","running = True\r","while running:\r","    for event in pygame.event.get():\r","        if event.type == pygame.QUIT:\r","            running = False\r","        elif event.type == pygame.KEYDOWN:\r","            if event.key == pygame.K_UP:\r","                ball_pos[1] = max(ball_pos[1] - 20, ball_radius)  # Ensure the ball stays inside the screen\r","            elif event.key == pygame.K_DOWN:\r","                ball_pos[1] = min(ball_pos[1] + 20, height - ball_radius)\r","            elif event.key == pygame.K_LEFT:\r","                ball_pos[0] = max(ball_pos[0] - 20, ball_radius)\r","            elif event.key == pygame.K_RIGHT:\r","                ball_pos[0] = min(ball_pos[0] + 20, width - ball_radius)\r","\r","    screen.fill((255, 255, 255)) \r","\r","    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)\r","\r","    pygame.display.flip()\r","\r","pygame.quit()\r","sys.exit()\r"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":11,"cssClass":"pl-en"}],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-c1"},{"start":21,"end":24,"cssClass":"pl-c1"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":15,"cssClass":"pl-s1"},{"start":16,"end":23,"cssClass":"pl-s1"},{"start":24,"end":32,"cssClass":"pl-en"},{"start":34,"end":39,"cssClass":"pl-s1"},{"start":41,"end":47,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":14,"cssClass":"pl-s1"},{"start":15,"end":26,"cssClass":"pl-en"},{"start":27,"end":40,"cssClass":"pl-s"}],[],[{"start":0,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":16,"cssClass":"pl-c1"}],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":14,"end":17,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":26,"end":32,"cssClass":"pl-c"}],[{"start":0,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"},{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":33,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":10,"end":14,"cssClass":"pl-c1"}],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":23,"cssClass":"pl-s1"},{"start":24,"end":29,"cssClass":"pl-s1"},{"start":30,"end":33,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":31,"cssClass":"pl-s1"},{"start":32,"end":36,"cssClass":"pl-v"}],[{"start":12,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":23,"cssClass":"pl-s1"},{"start":24,"end":26,"cssClass":"pl-c1"},{"start":27,"end":33,"cssClass":"pl-s1"},{"start":34,"end":41,"cssClass":"pl-v"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":20,"cssClass":"pl-s1"},{"start":21,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":34,"cssClass":"pl-s1"},{"start":35,"end":39,"cssClass":"pl-v"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-en"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":50,"cssClass":"pl-c1"},{"start":52,"end":63,"cssClass":"pl-s1"},{"start":66,"end":108,"cssClass":"pl-c"}],[{"start":12,"end":16,"cssClass":"pl-k"},{"start":17,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":36,"cssClass":"pl-s1"},{"start":37,"end":43,"cssClass":"pl-v"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-en"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":50,"cssClass":"pl-c1"},{"start":52,"end":58,"cssClass":"pl-s1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":61,"end":72,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-k"},{"start":17,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":36,"cssClass":"pl-s1"},{"start":37,"end":43,"cssClass":"pl-v"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-en"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":50,"cssClass":"pl-c1"},{"start":52,"end":63,"cssClass":"pl-s1"}],[{"start":12,"end":16,"cssClass":"pl-k"},{"start":17,"end":22,"cssClass":"pl-s1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":36,"cssClass":"pl-s1"},{"start":37,"end":44,"cssClass":"pl-v"}],[{"start":16,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-en"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":48,"end":50,"cssClass":"pl-c1"},{"start":52,"end":57,"cssClass":"pl-s1"},{"start":58,"end":59,"cssClass":"pl-c1"},{"start":60,"end":71,"cssClass":"pl-s1"}],[],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":15,"cssClass":"pl-en"},{"start":17,"end":20,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-c1"},{"start":27,"end":30,"cssClass":"pl-c1"}],[],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-en"},{"start":23,"end":29,"cssClass":"pl-s1"},{"start":31,"end":41,"cssClass":"pl-s1"},{"start":44,"end":47,"cssClass":"pl-en"},{"start":48,"end":56,"cssClass":"pl-s1"},{"start":57,"end":58,"cssClass":"pl-c1"},{"start":62,"end":65,"cssClass":"pl-en"},{"start":66,"end":74,"cssClass":"pl-s1"},{"start":75,"end":76,"cssClass":"pl-c1"},{"start":81,"end":92,"cssClass":"pl-s1"}],[],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":18,"cssClass":"pl-s1"},{"start":19,"end":23,"cssClass":"pl-en"}],[],[{"start":0,"end":6,"cssClass":"pl-s1"},{"start":7,"end":11,"cssClass":"pl-en"}],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":8,"cssClass":"pl-en"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/dlllnaz/PP2-Fall-2023/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/dlllnaz/PP2-Fall-2023/security/dependabot","repoSecurityAndAnalysisPath":"/dlllnaz/PP2-Fall-2023/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"3task.py","displayUrl":"https://github.com/dlllnaz/PP2-Fall-2023/blob/main/lab9/3task.py?raw=true","headerInfo":{"blobSize":"1.11 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"a6353f9","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fdlllnaz%2FPP2-Fall-2023%2Fblob%2Fmain%2Flab9%2F3task.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"33","truncatedSloc":"28"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/dlllnaz/PP2-Fall-2023/discussions/new","newIssuePath":"/dlllnaz/PP2-Fall-2023/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/dlllnaz/PP2-Fall-2023/blob/main/lab9/3task.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/dlllnaz/PP2-Fall-2023/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/dlllnaz/PP2-Fall-2023/raw/main/lab9/3task.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"dlllnaz","repoName":"PP2-Fall-2023","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"screen","kind":"constant","identStart":68,"identEnd":74,"extentStart":68,"extentEnd":117,"fullyQualifiedName":"screen","identUtf16":{"start":{"lineNumber":4,"utf16Col":0},"end":{"lineNumber":4,"utf16Col":6}},"extentUtf16":{"start":{"lineNumber":4,"utf16Col":0},"end":{"lineNumber":4,"utf16Col":49}}},{"name":"ball_radius","kind":"constant","identStart":164,"identEnd":175,"extentStart":164,"extentEnd":180,"fullyQualifiedName":"ball_radius","identUtf16":{"start":{"lineNumber":7,"utf16Col":0},"end":{"lineNumber":7,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":7,"utf16Col":0},"end":{"lineNumber":7,"utf16Col":16}}},{"name":"ball_color","kind":"constant","identStart":182,"identEnd":192,"extentStart":182,"extentEnd":206,"fullyQualifiedName":"ball_color","identUtf16":{"start":{"lineNumber":8,"utf16Col":0},"end":{"lineNumber":8,"utf16Col":10}},"extentUtf16":{"start":{"lineNumber":8,"utf16Col":0},"end":{"lineNumber":8,"utf16Col":24}}},{"name":"ball_pos","kind":"constant","identStart":215,"identEnd":223,"extentStart":215,"extentEnd":251,"fullyQualifiedName":"ball_pos","identUtf16":{"start":{"lineNumber":9,"utf16Col":0},"end":{"lineNumber":9,"utf16Col":8}},"extentUtf16":{"start":{"lineNumber":9,"utf16Col":0},"end":{"lineNumber":9,"utf16Col":36}}},{"name":"running","kind":"constant","identStart":255,"identEnd":262,"extentStart":255,"extentEnd":269,"fullyQualifiedName":"running","identUtf16":{"start":{"lineNumber":10,"utf16Col":0},"end":{"lineNumber":10,"utf16Col":7}},"extentUtf16":{"start":{"lineNumber":10,"utf16Col":0},"end":{"lineNumber":10,"utf16Col":14}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/dlllnaz/PP2-Fall-2023/branches":{"post":"THvxO3EhuVUEdRQ0rLGiCU3ledgNK-5P_acu4FCYnYwfV22WUU6a64YmQZABPz4uxdyeTnQeYYv1qwZWHmogSQ"},"/repos/preferences":{"post":"IcL1OdDP1QXuGV_VrC3zvlay4-xLUiBhwXt88tSkdd577DsLgdgc5klk7GtUkVoL4CijHcW1w-McK8EVrzmepg"}}},"title":"PP2-Fall-2023/lab9/3task.py at main · dlllnaz/PP2-Fall-2023"}