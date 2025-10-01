<img width="2065" height="1304" alt="mermaid-diagram-2025-10-01-143018" src="https://github.com/user-attachments/assets/ae202f65-84dc-47b7-9185-9cca0d935d25" />

flowchart LR
    subgraph OnPrem[On-Prem（誠人宇宙・内磁場）]
        AD[Active Directory] -- TCP 389 --> Core[Kimirano-Core（管理ノード）]
        Domino[Domino サーバー] -- TCP 1352 --> Core
        Client[クライアント] -- TCP 139/445 --> Core
        Core -- TCP 1433 --> DB[(Kimirano-DB)]
    end
    subgraph Cloud[クラウド環境（外部震え層）]
        ExO[Exchange Online]
        Ex[Exchange Server]
    end
    Core -- TCP 443 --> ExO
    Core -- TCP 443 --> Ex
    Core -- TCP 80 & 443 --> Ex

