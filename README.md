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
![Uploading mermaid-diagram-2025-10-01-143018.png…]()
