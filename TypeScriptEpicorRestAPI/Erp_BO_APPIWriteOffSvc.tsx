import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APPIWriteOffSvc
// Description: A/P Promissory Note Write Off Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get APPIWriteOffs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPIWriteOffs
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadRow
   */  
export function get_APPIWriteOffs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPIWriteOffs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPIWriteOffs(requestBody:Erp_Tablesets_APPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPIWriteOff item
   Description: Calls GetByID to retrieve the APPIWriteOff item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPIWriteOff
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNHeadRow
   */  
export function get_APPIWriteOffs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_APPNHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPIWriteOff for the service
   Description: Calls UpdateExt to update APPIWriteOff. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPIWriteOff
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPIWriteOffs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, requestBody:Erp_Tablesets_APPNHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete APPIWriteOff item
   Description: Call UpdateExt to delete APPIWriteOff item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPIWriteOff
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPIWriteOffs_Company_GroupID_HeadNum(Company:string, GroupID:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get APPNMoves items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNMoves1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveRow
   */  
export function get_APPIWriteOffs_Company_GroupID_HeadNum_APPNMoves(Company:string, GroupID:string, HeadNum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/APPNMoves", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNMove item
   Description: Calls GetByID to retrieve the APPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMove1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNMoveRow
   */  
export function get_APPIWriteOffs_Company_GroupID_HeadNum_APPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
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
         resolve(data as Erp_Tablesets_APPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APPNMoves items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNMoves
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveRow
   */  
export function get_APPNMoves(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNMoves
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNMoveRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPNMoves(requestBody:Erp_Tablesets_APPNMoveRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNMove item
   Description: Calls GetByID to retrieve the APPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMove
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNMoveRow
   */  
export function get_APPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNMoveRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
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
         resolve(data as Erp_Tablesets_APPNMoveRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPNMove for the service
   Description: Calls UpdateExt to update APPNMove. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNMove
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, requestBody:Erp_Tablesets_APPNMoveRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete APPNMove item
   Description: Call UpdateExt to delete APPNMove item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNMove
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPNMoves_Company_GroupID_HeadNum_Seq(Company:string, GroupID:string, HeadNum:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get APPNMoveTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNMoveTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveTGLCRow
   */  
export function get_APPNMoves_Company_GroupID_HeadNum_Seq_APPNMoveTGLCs(Company:string, GroupID:string, HeadNum:string, Seq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/APPNMoveTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNMoveTGLC item
   Description: Calls GetByID to retrieve the APPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMoveTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param Seq Desc: Seq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   */  
export function get_APPNMoves_Company_GroupID_HeadNum_Seq_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company:string, GroupID:string, HeadNum:string, Seq:string, SeqNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_APPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APPNMoveTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNMoveTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveTGLCRow
   */  
export function get_APPNMoveTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNMoveTGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPNMoveTGLCs(requestBody:Erp_Tablesets_APPNMoveTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNMoveTGLC item
   Description: Calls GetByID to retrieve the APPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMoveTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   */  
export function get_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company:string, GroupID:string, HeadNum:string, SeqNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNMoveTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_APPNMoveTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPNMoveTGLC for the service
   Description: Calls UpdateExt to update APPNMoveTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNMoveTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company:string, GroupID:string, HeadNum:string, SeqNum:string, SysRowID:string, requestBody:Erp_Tablesets_APPNMoveTGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete APPNMoveTGLC item
   Description: Call UpdateExt to delete APPNMoveTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNMoveTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company:string, GroupID:string, HeadNum:string, SeqNum:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get APPNLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNListRow
   */  
export function get_APPNLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APPNListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPNLists(requestBody:Erp_Tablesets_APPNListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APPNList item
   Description: Calls GetByID to retrieve the APPNList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APPNListRow
   */  
export function get_APPNLists_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APPNListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists(" + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_APPNListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPNList for the service
   Description: Calls UpdateExt to update APPNList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPNLists_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_APPNListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists(" + SysRowID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete APPNList item
   Description: Call UpdateExt to delete APPNList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNList
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPNLists_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists(" + SysRowID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:Erp_Tablesets_LegalNumGenOptsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseAPPNHead:string, whereClauseAPPNMove:string, whereClauseAPPNMoveTGLC:string, whereClauseAPPNList:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPPNHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNHead=" + whereClauseAPPNHead
   }
   if(typeof whereClauseAPPNMove!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNMove=" + whereClauseAPPNMove
   }
   if(typeof whereClauseAPPNMoveTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNMoveTGLC=" + whereClauseAPPNMoveTGLC
   }
   if(typeof whereClauseAPPNList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPPNList=" + whereClauseAPPNList
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(groupID:string, headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGLInterface
   Description: Call this method once to validate the G/L Interface.  This method checks for
GLSyst availability and if G/L is interfaced with A/P. If A/P is not interfaced
with G/L then user should be asked if okay to continue without posting to G/L.
This method will return a Message for the user if not interfaced else the Message
is blank. If the user do not wish to continue then exit this object. This method
also returns a logical flag to indicate if Posting to G/L.  This value should be
passed on to each new A/P Adjustment (APPNMove) record to process.
   OperationID: CheckGLInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGLInterface(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckGLInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/CheckGLInterface", {
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
         resolve(data as CheckGLInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPNoteExisted
   OperationID: CheckPNoteExisted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPNoteExisted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNoteExisted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPNoteExisted(requestBody:CheckPNoteExisted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPNoteExisted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/CheckPNoteExisted", {
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
         resolve(data as CheckPNoteExisted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPPNList
   OperationID: GetAPPNList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPPNList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPPNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPPNList(requestBody:GetAPPNList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPPNList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetAPPNList", {
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
         resolve(data as GetAPPNList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an APPNHead record that's for the
APPromNoteID supplied.
   OperationID: GetGroupIDForPI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGroupIDForPI(requestBody:GetGroupIDForPI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGroupIDForPI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetGroupIDForPI", {
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
         resolve(data as GetGroupIDForPI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNMove1
   Description: This method is to be used in place of GetNewAPPNMove.  This method asks for
vendor number and invoice number to link the A/P Invoice Header (APPNHead)
to A/P Invoice Adjustment (APPNMove).
   OperationID: GetNewAPPNMove1
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMove1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMove1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNMove1(requestBody:GetNewAPPNMove1_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNMove1_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetNewAPPNMove1", {
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
         resolve(data as GetNewAPPNMove1_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPNByID
   OperationID: GetPNByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPNByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPNByID(requestBody:GetPNByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPNByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetPNByID", {
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
         resolve(data as GetPNByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNHead(requestBody:GetNewAPPNHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetNewAPPNHead", {
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
         resolve(data as GetNewAPPNHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNMove
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNMove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNMove(requestBody:GetNewAPPNMove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNMove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetNewAPPNMove", {
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
         resolve(data as GetNewAPPNMove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPPNMoveTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNMoveTGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMoveTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMoveTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPPNMoveTGLC(requestBody:GetNewAPPNMoveTGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPPNMoveTGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetNewAPPNMoveTGLC", {
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
         resolve(data as GetNewAPPNMoveTGLC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/Update", {
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
         resolve(data as Update_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNMoveRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APPNMoveTGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow,
}

export interface Erp_Tablesets_APPNHeadListRow{
      /**  Applied Amount. Base Currency.  */  
   "AppliedAmount":number,
      /**  Bank Account of the promissory note.  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Bank Total Amount.  */  
   "BankTotalAmt":number,
      /**  Cash book Number.  */  
   "CashBookNum":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Bank Account ID of the company.  */  
   "CompBankAcctID":string,
      /**  Currency code of the promissory note.  */  
   "CurrencyCode":string,
      /**  Description  */  
   "Description":string,
      /**  Discount amount in base currency.  */  
   "DiscountAmt":number,
      /**  Promissory Note amount in document currency.  */  
   "DocPNAmt":number,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Entry Person.  */  
   "EntryPerson":string,
      /**  Exchange Rate of the promissory note.  */  
   "ExchangeRate":number,
      /**  Indicates if the promissory node is fully paid.  */  
   "Paid":boolean,
      /**  Promissory note amount in base currency.  */  
   "PNAmt":number,
      /**  Indicates that the promissory note is posted.  */  
   "Posted":boolean,
      /**  Rate Group Code.  */  
   "RateGrpCode":string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   "Rpt1PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   "Rpt1Discountamt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   "Rpt1BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   "Rpt2PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   "Rpt2DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   "Rpt2BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   "Rpt3PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   "Rpt3DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   "Rpt3BankTotalAmt":number,
      /**  Indicates that the promissory note is signed.  */  
   "Signed":boolean,
      /**  Total AP Amount  */  
   "TotalAPAmt":number,
      /**  Transaction date.  */  
   "TransDate":string,
      /**  Supplier Bank Account ID  */  
   "VendBankAcctID":string,
      /**  Supplier ID  */  
   "VendorID":string,
      /**  Supplier number  */  
   "VendorNum":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  AP Payment Instrument ID  */  
   "APPromNoteID":string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CompanyName":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  First supplier address line.  */  
   "SupplierAddr1":string,
      /**  Second supplier address line.  */  
   "SupplierAddr2":string,
      /**  Third supplier address line.  */  
   "SupplierAddr3":string,
      /**  Company City portion of the address.  */  
   "SupplierCity":string,
      /**  Supplier State portion of the address.  */  
   "SupplierState":string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   "SupplierPostalCode":string,
      /**  Supplier Name  */  
   "SupplierName":string,
      /**  Supplier Country portion of the address.  */  
   "SupplierCountry":string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   "PIStatus":string,
      /**  Promissory Note Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  IBAN Code for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Enter Totals flag  */  
   "IsEnterTotal":boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Reference to the first checkhed  */  
   "FirstHeadNum":number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   "Manual":boolean,
      /**  Reason to change the Customer or Company information  */  
   "ChgComment":string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   "PymtCntr":boolean,
      /**  Payment Instrument Stage  */  
   "PIStage":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  SupplierCountryNum  */  
   "SupplierCountryNum":number,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
   "BankCurrSymbol":string,
   "BaseCurrSymbol":string,
   "PaymentAmount":number,
   "PaymentStatus":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
   "VendBankName":string,
   "VendBankAcct":string,
   "VendBankIdentifier":string,
   "XRateLabel":string,
   "EnterPaymentTotal":boolean,
   "FullyPaid":boolean,
   "TotalRoundDiff":number,
   "XRateLabelPaymentBank":string,
   "XRateLabelPaymentBase":string,
   "VoidDate":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Field to bring the Company Country Name  */  
   "CompanyCountryNum":number,
   "TypeDesc":string,
   "IsFiltered":boolean,
   "GainLossReal":number,
   "DocGainLossReal":number,
   "Rpt1GainLossReal":number,
   "Rpt2GainLossReal":number,
   "Rpt3GainLossReal":number,
   "DocGainLossUnreal":number,
   "GainLossUnreal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3GainLossUnreal":number,
   "RevalDate":string,
   "DocDiscountAmt":number,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrSymbolDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrSymbolCurrName":string,
      /**  Description of the currency  */  
   "BaseCurrSymbolCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrSymbolCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrSymbolCurrencyID":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  Status Description  */  
   "PIStatusStatusDesc":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  Supplier Bank Name  */  
   "VendBankAcctIDBankName":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNHeadRow{
      /**  Applied Amount. Base Currency.  */  
   "AppliedAmount":number,
      /**  Bank Account of the promissory note.  */  
   "BankAcctID":string,
      /**  Bank Amount  */  
   "BankAmount":number,
      /**  Bank Slip Number of the promissory note.  */  
   "BankSlip":string,
      /**  Bank Total Amount.  */  
   "BankTotalAmt":number,
      /**  Cash book Number.  */  
   "CashBookNum":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Bank Account ID of the company.  */  
   "CompBankAcctID":string,
      /**  Currency code of the promissory note.  */  
   "CurrencyCode":string,
      /**  Description  */  
   "Description":string,
      /**  Discount amount in base currency.  */  
   "DiscountAmt":number,
      /**  Promissory Note amount in document currency.  */  
   "DocPNAmt":number,
      /**  Due date of the promissory note.  */  
   "DueDate":string,
      /**  Entry Person.  */  
   "EntryPerson":string,
      /**  Exchange Rate of the promissory note.  */  
   "ExchangeRate":number,
      /**  Indicates if the promissory node is fully paid.  */  
   "Paid":boolean,
      /**  Promissory note amount in base currency.  */  
   "PNAmt":number,
      /**  Indicates that the promissory note is posted.  */  
   "Posted":boolean,
      /**  Rate Group Code.  */  
   "RateGrpCode":string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   "Rpt1PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   "Rpt1Discountamt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   "Rpt1BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   "Rpt2PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   "Rpt2DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   "Rpt2BankTotalAmt":number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   "Rpt3PNAmt":number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   "Rpt3DiscountAmt":number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   "Rpt3BankTotalAmt":number,
      /**  Indicates that the promissory note is signed.  */  
   "Signed":boolean,
      /**  Total AP Amount  */  
   "TotalAPAmt":number,
      /**  Transaction date.  */  
   "TransDate":string,
      /**  Supplier Bank Account ID  */  
   "VendBankAcctID":string,
      /**  Supplier ID  */  
   "VendorID":string,
      /**  Supplier number  */  
   "VendorNum":number,
      /**  Voided Flag  */  
   "Voided":boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  AP Payment Instrument ID  */  
   "APPromNoteID":string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  First company address line.  */  
   "CompanyAddr1":string,
      /**  Second company address line.  */  
   "CompanyAddr2":string,
      /**  Third company address line.  */  
   "CompanyAddr3":string,
      /**  Company City portion of the address.  */  
   "CompanyCity":string,
      /**  Company Country portion of the address.  */  
   "CompanyCountry":string,
      /**  Company Name  */  
   "CompanyName":string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   "CompanyPostalCode":string,
      /**  Company State portion of the address.  */  
   "CompanyState":string,
      /**  First supplier address line.  */  
   "SupplierAddr1":string,
      /**  Second supplier address line.  */  
   "SupplierAddr2":string,
      /**  Third supplier address line.  */  
   "SupplierAddr3":string,
      /**  Company City portion of the address.  */  
   "SupplierCity":string,
      /**  Supplier State portion of the address.  */  
   "SupplierState":string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   "SupplierPostalCode":string,
      /**  Supplier Name  */  
   "SupplierName":string,
      /**  Supplier Country portion of the address.  */  
   "SupplierCountry":string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   "PIStatus":string,
      /**  Promissory Note Type  */  
   "Type":string,
      /**  Issue Date  */  
   "IssueDate":string,
      /**  IBAN Code for company's bank.  */  
   "CompIBANCode":string,
      /**  Bank/Branch Code for company's bank.  */  
   "CompBankBranchCode":string,
      /**  Bank/Branch Code for customer's bank.  */  
   "CustBankBranchCode":string,
      /**  IBAN Code for customer's bank.  */  
   "CustIBANCode":string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Enter Totals flag  */  
   "IsEnterTotal":boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   "ClearedAmt":number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   "ClearedPerson":string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPI":boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   "CashbookLine":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Reference to the first checkhed  */  
   "FirstHeadNum":number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   "Manual":boolean,
      /**  Reason to change the Customer or Company information  */  
   "ChgComment":string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   "PymtCntr":boolean,
      /**  Payment Instrument Stage  */  
   "PIStage":string,
      /**  Lock Exchange Rate  */  
   "LockRate":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  SupplierCountryNum  */  
   "SupplierCountryNum":number,
      /**  Reference to Endorsed AR PI GroupID.  */  
   "EndorsedARPNGroupID":string,
      /**  Reference to Endorsed AR PI HeadNum.  */  
   "EndorsedARPNHeadNum":number,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
   "BankCurrSymbol":string,
   "BankFeeAmt":number,
   "BankRecGainLoss":number,
   "BaseCurrSymbol":string,
   "CompanyBankAcct":string,
   "CompanyBankIdentifier":string,
   "CompanyBankName":string,
      /**  Field to bring the Company Country Name  */  
   "CompanyCountryNum":number,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
   "DocAllocAmt":number,
   "DocBankFeeAmt":number,
   "DocBankRecGainLoss":number,
   "DocDiscountAmt":number,
   "DocGainLossReal":number,
   "DocGainLossUnreal":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
   "EnterPaymentTotal":boolean,
   "FullyPaid":boolean,
   "GainLossReal":number,
   "GainLossUnreal":number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   "HasLegNumCnfg":boolean,
   "IsFiltered":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "PaymentAmount":number,
   "PaymentStatus":string,
   "RevalDate":string,
   "Rpt1AllocAmt":number,
   "Rpt1BankFeeAmt":number,
   "Rpt1BankRecGainLoss":number,
   "Rpt1GainLossReal":number,
   "Rpt1GainLossUnreal":number,
   "Rpt2AllocAmt":number,
   "Rpt2BankFeeAmt":number,
   "Rpt2BankRecGainLoss":number,
   "Rpt2GainLossReal":number,
   "Rpt2GainLossUnreal":number,
   "Rpt3AllocAmt":number,
   "Rpt3BankFeeAmt":number,
   "Rpt3BankRecGainLoss":number,
   "Rpt3GainLossReal":number,
   "Rpt3GainLossUnreal":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "StatusChgLegalNum":string,
   "StatusChgTranDocType":string,
   "TotalRoundDiff":number,
   "TypeDesc":string,
   "VendBankAcct":string,
   "VendBankIdentifier":string,
   "VendBankName":string,
   "VoidDate":string,
   "XRateLabel":string,
   "XRateLabelPaymentBank":string,
   "XRateLabelPaymentBase":string,
   "AllocAmt":number,
      /**  Endorsed AR PI Status  */  
   "EndorsedARPNStatus":string,
      /**  Endorsed AR PI Status Change Transaction Document Type.  */  
   "EndorsedARPNStatusChgTranDocType":string,
      /**  Endorsed AR PI Status Change Legal Number.  */  
   "EndorsedARPNStatusChgLegalNum":string,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "BaseCurrSymbolCurrencyID":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolDocumentDesc":string,
   "BaseCurrSymbolCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "PIStatusStatusDesc":string,
   "TranDocTypeDescription":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "VendorNumDefaultFOB":string,
   "VendorNumAddress3":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumAddress1":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumState":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNListRow{
   "APPromNoteID":string,
   "Company":string,
   "CurGroupID":string,
   "VendorID":string,
   "GroupID":string,
   "HeadNum":number,
   "PIStage":string,
   "PIStatus":string,
   "TranAPAmt":number,
   "Type":string,
      /**  To select row in grid  */  
   "Selected":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNMoveRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  Movement Order  */  
   "Seq":number,
      /**  Current Group ID  */  
   "CurGroupID":string,
      /**  Status  */  
   "PIStatus":string,
      /**  Stage  */  
   "PIStage":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  Date created  */  
   "CreateDate":string,
      /**  Created By User  */  
   "CreateUser":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Move Type  */  
   "Type":string,
      /**  Comment  */  
   "Comment":string,
      /**  Transaction date.  */  
   "TranDate":string,
      /**  Creation Time  */  
   "CreateTime":number,
      /**  Transaction Document Type for the record.  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description  */  
   "Description":string,
   "LegalNumMessage":string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   "LegalNumStyle":string,
      /**  Posting Error Message  */  
   "PostErrMess":string,
      /**  Indicates if posting GL transactions.  */  
   "PostToGL":boolean,
   "StatusDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APPNMoveTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  HeadNum for relation to APPNMoveTGLC  */  
   "HeadNum":number,
      /**  Seq for relation to APPNMoveTGLC  */  
   "Seq":number,
      /**  GroupID for relation to APPNMoveTGLC  */  
   "GroupID":string,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountGLShortAcct":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAcctDisp":string,
   "GLBookCurrencyCode":string,
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface CheckGLInterface_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opPostToGL:boolean,
}
}

   /** Required : 
      @param ipPIStage
      @param ipID
      @param ipVendID
   */  
export interface CheckPNoteExisted_input{
      /**  ipPIType  */  
   ipPIStage:string,
      /**  ipID  */  
   ipID:string,
      /**  ipVendID  */  
   ipVendID:string,
}

export interface CheckPNoteExisted_output{
parameters : {
      /**  output parameters  */  
   opRet:string,
}
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface DeleteByID_input{
   groupID:string,
   headNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APPIWriteOffTableset{
   APPNHead:Erp_Tablesets_APPNHeadRow[],
   APPNMove:Erp_Tablesets_APPNMoveRow[],
   APPNMoveTGLC:Erp_Tablesets_APPNMoveTGLCRow[],
   APPNList:Erp_Tablesets_APPNListRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APPNHeadListRow{
      /**  Applied Amount. Base Currency.  */  
   AppliedAmount:number,
      /**  Bank Account of the promissory note.  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Bank Total Amount.  */  
   BankTotalAmt:number,
      /**  Cash book Number.  */  
   CashBookNum:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Bank Account ID of the company.  */  
   CompBankAcctID:string,
      /**  Currency code of the promissory note.  */  
   CurrencyCode:string,
      /**  Description  */  
   Description:string,
      /**  Discount amount in base currency.  */  
   DiscountAmt:number,
      /**  Promissory Note amount in document currency.  */  
   DocPNAmt:number,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Entry Person.  */  
   EntryPerson:string,
      /**  Exchange Rate of the promissory note.  */  
   ExchangeRate:number,
      /**  Indicates if the promissory node is fully paid.  */  
   Paid:boolean,
      /**  Promissory note amount in base currency.  */  
   PNAmt:number,
      /**  Indicates that the promissory note is posted.  */  
   Posted:boolean,
      /**  Rate Group Code.  */  
   RateGrpCode:string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   Rpt1PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   Rpt1Discountamt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   Rpt1BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   Rpt2PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   Rpt2DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   Rpt2BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   Rpt3PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   Rpt3DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   Rpt3BankTotalAmt:number,
      /**  Indicates that the promissory note is signed.  */  
   Signed:boolean,
      /**  Total AP Amount  */  
   TotalAPAmt:number,
      /**  Transaction date.  */  
   TransDate:string,
      /**  Supplier Bank Account ID  */  
   VendBankAcctID:string,
      /**  Supplier ID  */  
   VendorID:string,
      /**  Supplier number  */  
   VendorNum:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  AP Payment Instrument ID  */  
   APPromNoteID:string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CompanyName:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  First supplier address line.  */  
   SupplierAddr1:string,
      /**  Second supplier address line.  */  
   SupplierAddr2:string,
      /**  Third supplier address line.  */  
   SupplierAddr3:string,
      /**  Company City portion of the address.  */  
   SupplierCity:string,
      /**  Supplier State portion of the address.  */  
   SupplierState:string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   SupplierPostalCode:string,
      /**  Supplier Name  */  
   SupplierName:string,
      /**  Supplier Country portion of the address.  */  
   SupplierCountry:string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   PIStatus:string,
      /**  Promissory Note Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  IBAN Code for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Enter Totals flag  */  
   IsEnterTotal:boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Reference to the first checkhed  */  
   FirstHeadNum:number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   Manual:boolean,
      /**  Reason to change the Customer or Company information  */  
   ChgComment:string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   PymtCntr:boolean,
      /**  Payment Instrument Stage  */  
   PIStage:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  SupplierCountryNum  */  
   SupplierCountryNum:number,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
   BankCurrSymbol:string,
   BaseCurrSymbol:string,
   PaymentAmount:number,
   PaymentStatus:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
   VendBankName:string,
   VendBankAcct:string,
   VendBankIdentifier:string,
   XRateLabel:string,
   EnterPaymentTotal:boolean,
   FullyPaid:boolean,
   TotalRoundDiff:number,
   XRateLabelPaymentBank:string,
   XRateLabelPaymentBase:string,
   VoidDate:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Field to bring the Company Country Name  */  
   CompanyCountryNum:number,
   TypeDesc:string,
   IsFiltered:boolean,
   GainLossReal:number,
   DocGainLossReal:number,
   Rpt1GainLossReal:number,
   Rpt2GainLossReal:number,
   Rpt3GainLossReal:number,
   DocGainLossUnreal:number,
   GainLossUnreal:number,
   Rpt1GainLossUnreal:number,
   Rpt2GainLossUnreal:number,
   Rpt3GainLossUnreal:number,
   RevalDate:string,
   DocDiscountAmt:number,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrSymbolDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrSymbolCurrName:string,
      /**  Description of the currency  */  
   BaseCurrSymbolCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrSymbolCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrSymbolCurrencyID:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  Status Description  */  
   PIStatusStatusDesc:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  Supplier Bank Name  */  
   VendBankAcctIDBankName:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNHeadListTableset{
   APPNHeadList:Erp_Tablesets_APPNHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APPNHeadRow{
      /**  Applied Amount. Base Currency.  */  
   AppliedAmount:number,
      /**  Bank Account of the promissory note.  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Bank Total Amount.  */  
   BankTotalAmt:number,
      /**  Cash book Number.  */  
   CashBookNum:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Bank Account ID of the company.  */  
   CompBankAcctID:string,
      /**  Currency code of the promissory note.  */  
   CurrencyCode:string,
      /**  Description  */  
   Description:string,
      /**  Discount amount in base currency.  */  
   DiscountAmt:number,
      /**  Promissory Note amount in document currency.  */  
   DocPNAmt:number,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Entry Person.  */  
   EntryPerson:string,
      /**  Exchange Rate of the promissory note.  */  
   ExchangeRate:number,
      /**  Indicates if the promissory node is fully paid.  */  
   Paid:boolean,
      /**  Promissory note amount in base currency.  */  
   PNAmt:number,
      /**  Indicates that the promissory note is posted.  */  
   Posted:boolean,
      /**  Rate Group Code.  */  
   RateGrpCode:string,
      /**  Promissory Note Amount in Report Currency 1.  */  
   Rpt1PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 1.  */  
   Rpt1Discountamt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 1.  */  
   Rpt1BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 2.  */  
   Rpt2PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 2.  */  
   Rpt2DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 2.  */  
   Rpt2BankTotalAmt:number,
      /**  Promissory Note Amount in Report Currency 3.  */  
   Rpt3PNAmt:number,
      /**  Promissory Note Discount Amount in Report Currency 3.  */  
   Rpt3DiscountAmt:number,
      /**  Promissory Note Bank Total Amount in Report Currency 3.  */  
   Rpt3BankTotalAmt:number,
      /**  Indicates that the promissory note is signed.  */  
   Signed:boolean,
      /**  Total AP Amount  */  
   TotalAPAmt:number,
      /**  Transaction date.  */  
   TransDate:string,
      /**  Supplier Bank Account ID  */  
   VendBankAcctID:string,
      /**  Supplier ID  */  
   VendorID:string,
      /**  Supplier number  */  
   VendorNum:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  AP Payment Instrument ID  */  
   APPromNoteID:string,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CompanyName:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  First supplier address line.  */  
   SupplierAddr1:string,
      /**  Second supplier address line.  */  
   SupplierAddr2:string,
      /**  Third supplier address line.  */  
   SupplierAddr3:string,
      /**  Company City portion of the address.  */  
   SupplierCity:string,
      /**  Supplier State portion of the address.  */  
   SupplierState:string,
      /**  Supplier Postal Code or Zip Code portion of the address.  */  
   SupplierPostalCode:string,
      /**  Supplier Name  */  
   SupplierName:string,
      /**  Supplier Country portion of the address.  */  
   SupplierCountry:string,
      /**   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  */  
   PIStatus:string,
      /**  Promissory Note Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  IBAN Code for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Enter Totals flag  */  
   IsEnterTotal:boolean,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Reference to the first checkhed  */  
   FirstHeadNum:number,
      /**  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  */  
   Manual:boolean,
      /**  Reason to change the Customer or Company information  */  
   ChgComment:string,
      /**  Indicates APPRomNoteID was generated using AP CheckHed numbering  */  
   PymtCntr:boolean,
      /**  Payment Instrument Stage  */  
   PIStage:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  SupplierCountryNum  */  
   SupplierCountryNum:number,
      /**  Reference to Endorsed AR PI GroupID.  */  
   EndorsedARPNGroupID:string,
      /**  Reference to Endorsed AR PI HeadNum.  */  
   EndorsedARPNHeadNum:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
   BankCurrSymbol:string,
   BankFeeAmt:number,
   BankRecGainLoss:number,
   BaseCurrSymbol:string,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
      /**  Field to bring the Company Country Name  */  
   CompanyCountryNum:number,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
   DocAllocAmt:number,
   DocBankFeeAmt:number,
   DocBankRecGainLoss:number,
   DocDiscountAmt:number,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
   EnterPaymentTotal:boolean,
   FullyPaid:boolean,
   GainLossReal:number,
   GainLossUnreal:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
   IsFiltered:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PaymentAmount:number,
   PaymentStatus:string,
   RevalDate:string,
   Rpt1AllocAmt:number,
   Rpt1BankFeeAmt:number,
   Rpt1BankRecGainLoss:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt2AllocAmt:number,
   Rpt2BankFeeAmt:number,
   Rpt2BankRecGainLoss:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt3AllocAmt:number,
   Rpt3BankFeeAmt:number,
   Rpt3BankRecGainLoss:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   StatusChgLegalNum:string,
   StatusChgTranDocType:string,
   TotalRoundDiff:number,
   TypeDesc:string,
   VendBankAcct:string,
   VendBankIdentifier:string,
   VendBankName:string,
   VoidDate:string,
   XRateLabel:string,
   XRateLabelPaymentBank:string,
   XRateLabelPaymentBase:string,
   AllocAmt:number,
      /**  Endorsed AR PI Status  */  
   EndorsedARPNStatus:string,
      /**  Endorsed AR PI Status Change Transaction Document Type.  */  
   EndorsedARPNStatusChgTranDocType:string,
      /**  Endorsed AR PI Status Change Legal Number.  */  
   EndorsedARPNStatusChgLegalNum:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   BaseCurrSymbolCurrencyID:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolDocumentDesc:string,
   BaseCurrSymbolCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   PIStatusStatusDesc:string,
   TranDocTypeDescription:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumDefaultFOB:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumAddress1:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumState:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNListRow{
   APPromNoteID:string,
   Company:string,
   CurGroupID:string,
   VendorID:string,
   GroupID:string,
   HeadNum:number,
   PIStage:string,
   PIStatus:string,
   TranAPAmt:number,
   Type:string,
      /**  To select row in grid  */  
   Selected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNMoveRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Movement Order  */  
   Seq:number,
      /**  Current Group ID  */  
   CurGroupID:string,
      /**  Status  */  
   PIStatus:string,
      /**  Stage  */  
   PIStage:string,
      /**  Posted  */  
   Posted:boolean,
      /**  Date created  */  
   CreateDate:string,
      /**  Created By User  */  
   CreateUser:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Move Type  */  
   Type:string,
      /**  Comment  */  
   Comment:string,
      /**  Transaction date.  */  
   TranDate:string,
      /**  Creation Time  */  
   CreateTime:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description  */  
   Description:string,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
      /**  Posting Error Message  */  
   PostErrMess:string,
      /**  Indicates if posting GL transactions.  */  
   PostToGL:boolean,
   StatusDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPNMoveTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  HeadNum for relation to APPNMoveTGLC  */  
   HeadNum:number,
      /**  Seq for relation to APPNMoveTGLC  */  
   Seq:number,
      /**  GroupID for relation to APPNMoveTGLC  */  
   GroupID:string,
   BitFlag:number,
   COADescription:string,
   GLAccountGLShortAcct:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLBookCurrencyCode:string,
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAPPIWriteOffTableset{
   APPNHead:Erp_Tablesets_APPNHeadRow[],
   APPNMove:Erp_Tablesets_APPNMoveRow[],
   APPNMoveTGLC:Erp_Tablesets_APPNMoveTGLCRow[],
   APPNList:Erp_Tablesets_APPNListRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipType
      @param ipPNID
      @param ipVendID
   */  
export interface GetAPPNList_input{
      /**  ipType  */  
   ipType:string,
      /**  ipPNID  */  
   ipPNID:string,
      /**  ipVendID  */  
   ipVendID:string,
}

export interface GetAPPNList_output{
   returnObj:Erp_Tablesets_APPIWriteOffTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetByID_input{
   groupID:string,
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APPIWriteOffTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APPIWriteOffTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APPIWriteOffTableset[],
}

   /** Required : 
      @param apPromNoteID
   */  
export interface GetGroupIDForPI_input{
      /**  AR Promissory Note ID  */  
   apPromNoteID:string,
}

export interface GetGroupIDForPI_output{
parameters : {
      /**  output parameters  */  
   groupID:string,
   headNum:number,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_APPNHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewAPPNHead_input{
   ds:Erp_Tablesets_APPIWriteOffTableset[],
   groupID:string,
}

export interface GetNewAPPNHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPIWriteOffTableset,
}
}

   /** Required : 
      @param ds
      @param ipGroupID
      @param ipHeadNum
   */  
export interface GetNewAPPNMove1_input{
   ds:Erp_Tablesets_APPIWriteOffTableset[],
      /**  The Group ID for this A/P Promissory Note Head  */  
   ipGroupID:string,
      /**  The A/P Promissory Note Head Number  */  
   ipHeadNum:number,
}

export interface GetNewAPPNMove1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPIWriteOffTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
      @param seqNum
   */  
export interface GetNewAPPNMoveTGLC_input{
   ds:Erp_Tablesets_APPIWriteOffTableset[],
   groupID:string,
   headNum:number,
   seqNum:number,
}

export interface GetNewAPPNMoveTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPIWriteOffTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param headNum
   */  
export interface GetNewAPPNMove_input{
   ds:Erp_Tablesets_APPIWriteOffTableset[],
   groupID:string,
   headNum:number,
}

export interface GetNewAPPNMove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPIWriteOffTableset,
}
}

   /** Required : 
      @param ipHeadNum
      @param ipPIType
      @param ipID
      @param ipVendID
      @param ipCurGroupID
      @param ipNewPIType
      @param ds
   */  
export interface GetPNByID_input{
      /**  ipHeadNum  */  
   ipHeadNum:number,
      /**  ipPIType  */  
   ipPIType:string,
      /**  ipID  */  
   ipID:string,
      /**  ipVendID  */  
   ipVendID:string,
      /**  ipCurGroupID  */  
   ipCurGroupID:string,
      /**  ipNewPIType  */  
   ipNewPIType:string,
   ds:Erp_Tablesets_APPIWriteOffTableset[],
}

export interface GetPNByID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPIWriteOffTableset,
}
}

   /** Required : 
      @param whereClauseAPPNHead
      @param whereClauseAPPNMove
      @param whereClauseAPPNMoveTGLC
      @param whereClauseAPPNList
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPPNHead:string,
   whereClauseAPPNMove:string,
   whereClauseAPPNMoveTGLC:string,
   whereClauseAPPNList:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APPIWriteOffTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPPIWriteOffTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPPIWriteOffTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APPIWriteOffTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPIWriteOffTableset,
}
}

