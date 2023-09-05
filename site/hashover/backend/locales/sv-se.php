<?php

// Copyright (C) 2021 Jonathan Petersson, Jacob Barkdull
// This file is part of HashOver.
//
// I, Jacob Barkdull, hereby release this work into the public domain.
// This applies worldwide. If this is not legally possible, I grant any
// entity the right to use this work for any purpose, without any
// conditions, unless such conditions are required by law.


// Swedish text for forms, buttons, links, and tooltips
$locale = array (
	'comment-form'		=> 'Skriv kommentar här...',
	'reply-form'		=> 'Skriv svar här...',
	'comment-formatting'	=> 'Formatering',
	'allowed-html'		=> 'Tillåten HTML',
	'allowed-markdown'	=> 'Markdown Format',
	'html-format'		=> '&lt;b&gt;, &lt;strong&gt;, &lt;u&gt;, &lt;i&gt;, &lt;em&gt;, &lt;s&gt;, &lt;big&gt;, &lt;small&gt;, &lt;sup&gt;, &lt;sub&gt;, &lt;pre&gt;, &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;, &lt;blockquote&gt;, &lt;code&gt; undkommer HTML, URLer blir automatiskt länkar, och [img]URL här[/img] visar en extern bild.',
	'markdown-format'	=> '**Bold**, _underline_, *italic*, ~~strikethrough~~, `highlight`, ```code``` undkommer HTML. HTML och Markdown kan användas samtidigt i din kommentar.',
	'post-button'		=> 'Posta kommentar',
	'login'			=> 'Logga in',
	'login-tip'		=> 'Logga in (valfritt)',
	'logout'		=> 'Logga ut',
	'be-first-name'		=> 'Inga kommentarer ännu.',
	'pending-name'		=> 'Väntande...',
	'deleted-name'		=> 'Borttagen...',
	'error-name'		=> 'Fel...',
	'be-first-note'		=> 'Bli den första att kommentera!',
	'login-required'	=> 'Du måste vara inloggad för att kommentera!',
	'pending-note'		=> 'Denna kommentar väntar på godkännande.',
	'deleted-note'		=> 'Denna kommentar har tagits bort.',
	'error-note'		=> 'Något blev fel. Denna kommentar kunde ej visas.',
	'options'		=> 'Alternativ',
	'cancel'		=> 'Avbryt',
	'reply-to-comment'	=> 'Svara på kommentar',
	'edit-your-comment'	=> 'Redigera din kommentar',
	'optional'		=> 'Valfri',
	'required'		=> 'Obligatorisk',
	'name'			=> 'Namn',
	'name-tip'		=> 'Namn (%s)',
	'password'		=> 'Lösenord',
	'password-tip'		=> 'Lösenord (%s, gör att du kan redigera eller ta bort denna kommentar)',
	'confirm-password'	=> 'Bekräfta lösenord',
	'email'			=> 'E-postadress',
	'email-tip'		=> 'E-postadress (%s, för e-postnotifikation)',
	'website'		=> 'Webbsida',
	'websites'		=> 'Webbsidor',
	'website-tip'		=> 'Webbsida (%s)',
	'logged-in'		=> 'Du har loggat in!',
	'logged-out'		=> 'Du har loggat ut!',
	'comment-needed'	=> 'Du misslyckades med att ange en korrekt kommentar. Vänligen försök igen.',
	'reply-needed'		=> 'Du misslyckades med att ange ett korrekt svar. Vänligen försök igen.',
	'field-needed'		=> 'Följande fält "%s" är obligatoriskt.',
	'post-fail'		=> 'Fel! Du saknar tillräcklig behörighet.',
	'comment-deleted'	=> 'Kommentar borttagen!',
	'post-reply'		=> 'Posta svar',
	'delete'		=> 'Ta bort',
	'permanently-delete'	=> 'Ta bort permanent',
	'subscribe'		=> 'Meddela mig vid svar',
	'subscribe-tip'		=> 'Prenumerera på e-postnotifikationer',
	'edit-comment'		=> 'Redigera kommentar',
	'status'		=> 'Status',
	'status-approved'	=> 'Godkänd',
	'status-pending'	=> 'Väntar på godkännande',
	'status-deleted'	=> 'Markerad som borttagen',
	'save'			=> 'Spara',
	'no-email-warning'	=> 'Du kommer inte att få meddelande om svar på din kommentar utan att ange en e-postadress.',
	'invalid-email'		=> 'E-postadressen du angav är ogiltig.',
	'delete-comment'	=> 'Är du säker på att du vill ta bort denna kommentar?',
	'post-a-comment'	=> 'Posta en kommentar',
	'post-a-comment-on'	=> 'Posta en kommentar på "%s"',
	'most-popular-comment'	=> 'Most Popular Comment',
	'most-popular-comments'	=> 'Most Popular Comments',
	'showing-comment'	=> '%d Kommentar',
	'showing-comments'	=> '%d Kommentarer',
	'counting-reply'	=> '%d räknar svar',
	'counting-replies'	=> '%d räknar svar',
	'sort'			=> 'Sortera',
	'sort-ascending'	=> 'I ordningsföljd',
	'sort-descending'	=> 'I omvänd ordning',
	'sort-by-date'		=> 'Nyast först',
	'sort-by-likes'		=> 'Efter gillningar',
	'sort-by-replies'	=> 'Efter svar',
	'sort-by-discussion'	=> 'Efter diskussion',
	'sort-by-popularity'	=> 'Efter populäritet',
	'sort-by-name'		=> 'Efter kommentator',
	'threads'		=> 'Trådar',
	'in-reply-to'		=> 'Som svar på %s',
	'thread-tip'		=> 'Hoppa till toppen av tråden',
	'comments'		=> 'Kommentarer',
	'replies'		=> 'Svar',
	'edit'			=> 'Redigera',
	'reply'			=> 'Svara',
	'like'			=> 'Gilla',
	'likes'			=> 'Gillningar',
	'liked'			=> 'Gillad',
	'unlike'		=> 'Sluta gilla',
	'like-comment'		=> 'Gilla denna kommentar',
	'liked-comment'		=> 'Sluta gilla denna kommentar',
	'dislike'		=> 'Ogilla',
	'dislikes'		=> 'Ogillningar',
	'disliked'		=> 'Ogillad',
	'dislike-comment'	=> 'Ogilla denna kommentar',
	'disliked-comment'	=> 'Du ogillade denna kommentar',
	'commenter-tip'		=> 'Du kommer inte att meddelas via e-post',
	'subscribed-tip'	=> 'kommer att meddelas via e-post',
	'unsubscribed-tip'	=> 'prenumererar inte på e-postnotifikationer',
	'show-other-comment'	=> 'Visa %d annan kommentar',
	'show-other-comments'	=> 'Visa %d andra kommentarer',
	'show-comment'		=> 'Visa %d kommentar',
	'show-comments'		=> 'Visa %d kommentarer',
	'date-year'		=> '%d år sedan',
	'date-years'		=> '%d år sedan',
	'date-month'		=> '%d månad sedan',
	'date-months'		=> '%d månader sedan',
	'date-day'		=> '%d dag sedan',
	'date-days'		=> '%d dagar sedan',
	'date-today'		=> '%s idag',
	'untitled'		=> 'Utan titel',
	'external-image-tip'	=> 'Klicka för att visa extern bild',
	'loading'		=> 'Laddar...',
	'click-to-close'	=> 'Klicka för att stänga',
	'hashover-comments'	=> 'HashOver Kommentarer',
	'rss-feed'		=> 'RSS-flöde',
	'source-code'		=> 'Källkod',
	'new-comment'		=> 'Ny kommentar',
	'from'			=> 'Från %s',
	'comment'		=> 'Kommentar',
	'page'			=> 'Sida',
	'sent-by'		=> 'Detta e-oostmeddelande skickades av %s via HashOver.',
	'enabled'		=> 'Aktiverad',
	'disabled'		=> 'Inaktiverad',

	'source-code-sub'	=> 'HashOver server-side källkodsvisare',
	'type'			=> 'Typ',
	'path'			=> 'Sökväg',
	'view-as'		=> 'Visa som',
	'text'			=> 'Text',
	'download'		=> 'Ladda ner',

	'documentation'		=> 'Dokumentation',
	'coming-soon'		=> 'Kommer snart',
	'example'		=> 'Exempel',
	'back'			=> 'Tillbaka',
	'value'			=> 'Värde',

	'successful-save'	=> 'Sparat!',
	'failed-to-save'	=> 'Misslyckades att spara! Kontrollera behörigheter.',
	'permissions-info'	=> 'Ge "%s" behörighet 0755 och ägarskap till "%s" användaren.',

	'admin'			=> 'Admin',
	'moderation'		=> 'Moderering',
	'block-ip-addresses'	=> 'IP-blockering',
	'filter-url-queries'	=> 'URL-filtrering',
	'settings'		=> 'Inställningar',
	'check-for-updates'	=> 'Uppdateringar',

	'admin-required'	=> 'Du måste vara inloggad som admin',

	'blocklist-title'	=> 'Blockera IP-adresser',
	'blocklist-sub'		=> 'Blockera specifika IP-adresser',
	'blocklist-ip-tip'	=> 'IP-adress eller tomt för att radera',

	'url-queries-title'	=> 'Filtrera URL-frågor',
	'url-queries-sub'	=> 'Filtrera vilka URL-frågor som bör ignoreras',
	'url-queries-name-tip'	=> 'Frågans namn eller tomt för att radera',
	'url-queries-value-tip'	=> 'Frågans värde eller tomt för vilket värde som helst',

	'settings-sub'		=> 'Ändra diverse inställningar',
	'moderation-sub'	=> 'Posta, redigera, godkänna, och ta bort kommentarer',
	'no-threads'		=> 'Inga trådar hittades. Skapa en genom att använda HashOver på en av dina webbsidor och posta en kommentar.',

	'general'		=> 'Allmänt',
	'e-mail'		=> 'E-post',
	'cookies'		=> 'Cookies',
	'comment-collapsing'	=> 'Kollapsa kommentarer',
	'popular-comments'	=> 'Populära kommentarer',
	'spam-protection'	=> 'Spamskydd',
	'avatars'		=> 'Avatarer',
	'form-fields'		=> 'Formulär/Fält',
	'date-time'		=> 'Datum/Tid',
	'technical'		=> 'Tekniskt',

	'setting-language'			=> 'Språk',
	'setting-theme'				=> 'Tema',
	'setting-default-sorting'		=> 'Standard sorteringsordning för kommentarer',
	'setting-uses-moderation'		=> 'Kommentarer som postats av vanliga användare kräver moderering',
	'setting-pends-user-edits'		=> 'Kommentarer redigerade av vanliga användare kräver moderering',
	'setting-data-format'			=> 'Kommentar dataformat',
	'setting-sends-notifications'		=> 'Skicka e-postnotifikation till',
	'setting-mailer'			=> 'Leveransmetod för avisering via e-post',
	'setting-mail-type'			=> 'Format för e-postmeddelanden',
	'setting-default-name'			=> 'Standardnamn för kommentator',
	'setting-allows-images'			=> 'Tillåt visning av bilder i kommentarer',
	'setting-allows-login'			=> 'Tillåt användare att logga in',
	'setting-allows-likes'			=> 'Tillåt användare att gilla kommentarer',
	'setting-allows-dislikes'		=> 'Tillåt användare att ogilla kommentarer',
	'setting-uses-ajax'			=> 'Aktivera asynkrona JavaScript-funktioner',
	'setting-collapses-interface'		=> 'Kollapsa hela HashOvers användargränssnitt',
	'setting-collapses-comments'		=> 'Kollapsa ett konfigurerbart antal kommentarer',
	'setting-collapse-limit'		=> 'Antal kommentarer att kollapsa',
	'setting-reply-mode'			=> 'Visningsläge för kommentarstrådar',
	'setting-stream-depth'			=> 'Antal svarsindrag innan strömmen plattas ut',
	'setting-popularity-threshold'		=> 'Nettoantal gillningar som en kommentar måste uppnå för att vara populär',
	'setting-popularity-limit'		=> 'Antal populära kommentarer att visa',
	'setting-uses-markdown'			=> 'Aktivera Markdown support',
	'setting-server-timezone'		=> 'Server tidszon',
	'setting-uses-user-timezone'		=> 'Display dates/times in user\'s timezone (JavaScript-mode)',
	'setting-uses-short-dates'		=> 'Aktivera kortare datum/tider (exempel "1 dag sedan")',
	'setting-time-pattern'			=> 'Tidsformat, använd "HH:mm" för 24-timmars tid',
	'setting-date-pattern'			=> 'Datumformat',
	'setting-time-format'			=> 'Tidsformat, använd "H:i" för 24-timmars tid',
	'setting-date-format'			=> 'Datumformat',
	'setting-displays-title'		=> 'Aktivera visning av sidtitel',
	'setting-form-position'			=> 'Position för det huvudsakliga kommentarsformuläret',
	'setting-uses-auto-login'		=> 'Logga in användare automatiskt när de postar kommentarer',
	'setting-shows-reply-count'		=> 'Visa antalet svar separat från det totala antalet',
	'setting-counts-deletions'		=> 'Inkludera borttagna kommentarer i kommentarsräkningen',
	'setting-icon-mode'			=> 'Avatarikon visningsläge',
	'setting-icon-size'			=> 'Avatarikonens storlek',
	'setting-image-format'			=> 'Format för ikoner och andra bilder',
	'setting-uses-labels'			=> 'Visa etiketter ovanför inmatning',
	'setting-uses-cancel-buttons'		=> 'Visa avbryt-knappar i kommentarsformulär',
	'setting-appends-css'			=> 'Lägg automatiskt till HashOver CSS till sidan',
	'setting-appends-rss'			=> 'Lägg till HashOver RSS-flöde länkar till sidan',
	'setting-login-method'			=> 'Användare inloggningssystem',
	'setting-sets-cookies'			=> 'Aktivera cookies',
	'setting-cookie-expiration'		=> 'Relativt utgångsdatum för cookie',
	'setting-secure-cookies'		=> 'Använd endast säkra HTTPS-cookies',
	'setting-stores-ip-address'		=> 'Aktivera lagring av användarens IP-adresser',
	'setting-subscribes-user'		=> 'Som standard prenumererar användaren på e-postmeddelanden',
	'setting-allows-user-replies'		=> 'Ställ in användarens e-post som "Svara till" i svarsmeddelanden',
	'setting-noreply-email'			=> 'E-postadress som används i e-postmeddelanden till vanliga användare',
	'setting-spam-database'			=> 'Lokalisering för SPAM-databas',
	'setting-spam-check-modes'		=> 'Lägen för att utföra SPAM-kontroll under',
	'setting-gravatar-force'		=> 'Använd gravatarbilder med teman istället för avatarer',
	'setting-gravatar-default'		=> 'Standard Gravatar-tema som ska användas',
	'setting-minifies-javascript'		=> 'Aktivera JavaScript-minifiering',
	'setting-minify-level'			=> 'JavaScript minifieringsnivå',
	'setting-local-metadata'		=> 'Tillåt att sidans metadata uppdateras från localhost',
	'setting-name-field'			=> 'Namnfält för användare',
	'setting-password-field'		=> 'Fält för användarlösenord, för redigeringsbehörighet',
	'setting-email-field'			=> 'Fält för e-postnotifikationer för användare',
	'setting-website-field'			=> 'URL-fält för användarens webbsida'
);