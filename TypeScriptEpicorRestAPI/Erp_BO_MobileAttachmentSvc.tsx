import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MobileAttachmentSvc
// Description: 
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetDocumentTypes
   Description: Retrieve document types  valid for
   OperationID: GetDocumentTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDocumentTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDocumentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDocumentTypes(requestBody:GetDocumentTypes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDocumentTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/GetDocumentTypes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDocumentTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVersion
   Description: Returns BO Version
   OperationID: GetVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVersion(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileAttachmentSvc/GetVersion", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetVersion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_MobileAttachmentTableset{
   MobileXFileAttch:Erp_Tablesets_MobileXFileAttchRow[],
   MobileDocType:Erp_Tablesets_MobileDocTypeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MobileDocTypeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Unique identifier of a DocType. Assigned by the user.
Cannot be blank.  */  
   DocTypeID:string,
      /**  Full description of the DocType.  */  
   Description:string,
      /**   Indicates if the document type is one that would fullfill the rule that receipt documents be attached for inventory receipts of a Part Lot for a Part that has Part.RecDocReq = Yes  Defaults as No.
These required documents are duplicate from the receipt detail to the part lot.  */  
   Receipt:boolean,
      /**   Indicates if the document type is one that would fullfill the rule that shipping documents be attached before allowing the user
to set the ShipDocAvail flag on the PartLot or Job. (See Part.ShipDocAvail)  */  
   Shipment:boolean,
      /**  Optional. But if given, used as intial default to the attachement filename field. Note this is expressed in the CLient OS format (MS Windows). Usually using  UNC naming convention or common mapped drive  */  
   BaseURL:string,
      /**  The unique ID assigned by the Sharepoint system to attachments.  Field not required  */  
   SharePointID:string,
      /**  Storage Type  */  
   StorageType:number,
      /**  Image Name  */  
   ImageName:string,
      /**  Specific Tables  */  
   SpecificTables:boolean,
      /**  Marks this DocType as global, available to be sent out to other companies.  */  
   GlobalDocType:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  FileTransferMode  */  
   FileTransferMode:number,
      /**  AuthType  */  
   AuthType:string,
      /**  DirectoryID  */  
   DirectoryID:string,
      /**  ApplicationID  */  
   ApplicationID:string,
      /**  CertificateThumbPrint  */  
   CertificateThumbPrint:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileXFileAttchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  RelatedToSchemaName  */  
   RelatedToSchemaName:string,
      /**   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  */  
   Key4:string,
      /**   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  */  
   AttachNum:number,
      /**   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  */  
   Key5:string,
      /**  Foreign Key to XFileRef record.  */  
   XFileRefNum:number,
      /**  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  */  
   DoTrigger:boolean,
      /**  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  */  
   DupToRelatedToFile:string,
      /**  See DupToRelatedToFile  */  
   DupToKey1:string,
      /**  See DupToRelatedToFile  */  
   DupToKey2:string,
      /**  See DupToRelatedToFile  */  
   DupToKey3:string,
      /**  See DupToRelatedToFile  */  
   DupToKey4:string,
      /**  See DupToRelatedToFile  */  
   DupToKey5:string,
      /**  See DupToRelatedToFile  */  
   DupToAttachNum:number,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  The unique ID assigned by the Sharepoint system to attachments.  Field not required  */  
   SharePointID:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param tableName
   */  
export interface GetDocumentTypes_input{
   tableName:string,
}

export interface GetDocumentTypes_output{
   returnObj:Erp_Tablesets_MobileAttachmentTableset[],
}

export interface GetVersion_output{
   returnObj:string,
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

