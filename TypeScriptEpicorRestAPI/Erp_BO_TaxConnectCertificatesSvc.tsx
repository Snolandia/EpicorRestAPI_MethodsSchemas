import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TaxConnectCertificatesSvc
// Description: Business Object that handled Tax Connect Certificate Logic
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetTaxConnectCertificates
   Description: Retrieves list of Avalara CertCapture Certificates for a specific customer.
   OperationID: GetTaxConnectCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxConnectCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxConnectCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxConnectCertificates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/GetTaxConnectCertificates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DownloadTaxConnectCertificatePreview
   Description: Get the first page of the Certificate
   OperationID: DownloadTaxConnectCertificatePreview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadTaxConnectCertificatePreview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadTaxConnectCertificatePreview_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadTaxConnectCertificatePreview(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/DownloadTaxConnectCertificatePreview", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendCustomerToTaxConnect
   Description: Upload customer information to Avalara
   OperationID: SendCustomerToTaxConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendCustomerToTaxConnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendCustomerToTaxConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendCustomerToTaxConnect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/SendCustomerToTaxConnect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RequestTaxConnectCertificateCustomerInvite
   Description: Trigger an email certificate invite from avalara to the customer
   OperationID: RequestTaxConnectCertificateCustomerInvite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestTaxConnectCertificateCustomerInvite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestTaxConnectCertificateCustomerInvite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RequestTaxConnectCertificateCustomerInvite(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxConnectCertificatesSvc/RequestTaxConnectCertificateCustomerInvite", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param certificateID
   */  
export interface DownloadTaxConnectCertificatePreview_input{
      /**  Avalara Certificate ID  */  
   certificateID:number,
}

export interface DownloadTaxConnectCertificatePreview_output{
      /**  Certificate first page in base64  */  
   returnObj:string,
}

export interface Erp_Tablesets_TaxConnectCertificatesRow{
      /**  Description of business for the certificate. For example, Retail trade, Professional services, or Construction.  */  
   BusinessNumberType:string,
      /**  Unique ID number of this certificate.  */  
   CertificateID:number,
      /**  The date/time when this record was created.  */  
   CreatedDate:string,
      /**  This value is true if there exists a scanned PDF copy of this certificate or the PDF version of the form that the customer filled via the CertCapture wizard on S3 bucket.  */  
   DocumentExists:boolean,
      /**  Indicates the tax number passed in for the certificate.  */  
   ExemptionNumber:string,
      /**   If this certificate provides exemption from transactional taxes, what percentage of the transaction is considered exempt?

For a fully exempt certificate, this percentage should be 100.  */  
   ExemptPercentage:number,
      /**  The exemption reason associated with this certificate. For example, the reason code for exemption for purposes of resale is RESALE.  */  
   ExemptReason:string,
      /**  Expiration date when this certificate will no longer be valid.  */  
   ExpirationDate:string,
      /**  File name for the image of this certificate.  */  
   Filename:string,
      /**  The date/time when this record was last modified.  */  
   ModifiedDate:string,
      /**  Number of pages contained within this certificate.  */  
   PageCount:number,
      /**  The exposure zone/region where this certificate is valid.  */  
   Region:string,
      /**  The date when this certificate was signed.  */  
   SignedDate:string,
      /**  The status of the certificate  */  
   Status:string,
      /**  The tax number type for the certificate. For example, FEIN, Social Security Number, or Employer Identification Number.  */  
   TaxNumberType:string,
      /**  True if this certificate is marked as valid. A valid certificate can be considered for exemption purposes. When a certificate is marked invalid, it will no longer be considered when calculating exemption for a customer.  */  
   Valid:boolean,
      /**  The exemption reason that CertCapture audit/internal logic identifies for created certificate.  */  
   ValidatedExemptReason:string,
      /**  This value is true if the certificate has gone through the certificate validation process.  */  
   Verified:boolean,
      /**  Is this document limited to one document/order/invoice?  */  
   SingleUse:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxConnectCertificatesTableset{
   TaxConnectCertificates:Erp_Tablesets_TaxConnectCertificatesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param custNum
   */  
export interface GetTaxConnectCertificates_input{
      /**  Customer Number  */  
   custNum:number,
}

export interface GetTaxConnectCertificates_output{
   returnObj:Erp_Tablesets_TaxConnectCertificatesTableset[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

   /** Required : 
      @param custNum
   */  
export interface RequestTaxConnectCertificateCustomerInvite_input{
      /**  Customer Number  */  
   custNum:number,
}

export interface RequestTaxConnectCertificateCustomerInvite_output{
      /**  Message if invite link was generated/sent successfully  */  
   returnObj:string,
}

   /** Required : 
      @param custNum
   */  
export interface SendCustomerToTaxConnect_input{
      /**  Customer Number  */  
   custNum:number,
}

export interface SendCustomerToTaxConnect_output{
      /**  Message if upload was successful  */  
   returnObj:string,
}

