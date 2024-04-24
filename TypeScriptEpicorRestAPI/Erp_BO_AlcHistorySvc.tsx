import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AlcHistorySvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistories
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistRow
   */  
export function get_AlcHistories(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistories(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories", {
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
   Summary: Calls GetByID to retrieve the AlcHistory item
   Description: Calls GetByID to retrieve the AlcHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistory for the service
   Description: Calls UpdateExt to update AlcHistory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistories_Company_BatchID_RunNbr_AllocID(Company:string, BatchID:string, RunNbr:string, AllocID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistory item
   Description: Call UpdateExt to delete AlcHistory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistory
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistories_Company_BatchID_RunNbr_AllocID(Company:string, BatchID:string, RunNbr:string, AllocID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get AHGLJrnDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AHGLJrnDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtls(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AHGLJrnDtl item
   Description: Calls GetByID to retrieve the AHGLJrnDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AHGLJrnDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AHGLJrnDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AHGLJrnDtlSims items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AHGLJrnDtlSims1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlSimRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtlSims(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtlSims", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AHGLJrnDtlSim item
   Description: Calls GetByID to retrieve the AHGLJrnDtlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtlSim1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AHGLJrnDtlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AHGLJrnDtlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistAccts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistAcctRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistAccts(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistAcct item
   Description: Calls GetByID to retrieve the AlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistAcct1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistActCats items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistActCats1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistActCatRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistActCats(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistActCats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistActCat item
   Description: Calls GetByID to retrieve the AlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistActCat1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistDtlRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistDtls(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistDtl item
   Description: Calls GetByID to retrieve the AlcHistDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistJrnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistJrnCds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistJrnCdRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistJrnCds(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistJrnCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistJrnCd item
   Description: Calls GetByID to retrieve the AlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistJrnCd1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistParams(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistParam item
   Description: Calls GetByID to retrieve the AlcHistParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistRanges items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistRanges1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistRangeRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistRanges(Company:string, BatchID:string, RunNbr:string, AllocID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistRanges", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistRange item
   Description: Calls GetByID to retrieve the AlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistRange1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   */  
export function get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AHGLJrnDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AHGLJrnDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlRow
   */  
export function get_AHGLJrnDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AHGLJrnDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AHGLJrnDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls", {
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
   Summary: Calls GetByID to retrieve the AHGLJrnDtl item
   Description: Calls GetByID to retrieve the AHGLJrnDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   */  
export function get_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AHGLJrnDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AHGLJrnDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AHGLJrnDtl for the service
   Description: Calls UpdateExt to update AHGLJrnDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AHGLJrnDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AHGLJrnDtl item
   Description: Call UpdateExt to delete AHGLJrnDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AHGLJrnDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AHGLJrnDtlSims items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AHGLJrnDtlSims
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlSimRow
   */  
export function get_AHGLJrnDtlSims(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AHGLJrnDtlSims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AHGLJrnDtlSims(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims", {
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
   Summary: Calls GetByID to retrieve the AHGLJrnDtlSim item
   Description: Calls GetByID to retrieve the AHGLJrnDtlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtlSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   */  
export function get_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AHGLJrnDtlSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AHGLJrnDtlSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AHGLJrnDtlSim for the service
   Description: Calls UpdateExt to update AHGLJrnDtlSim. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AHGLJrnDtlSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AHGLJrnDtlSim item
   Description: Call UpdateExt to delete AHGLJrnDtlSim item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AHGLJrnDtlSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param Reverse Desc: Reverse   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, Reverse:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistAcctRow
   */  
export function get_AlcHistAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistAccts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts", {
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
   Summary: Calls GetByID to retrieve the AlcHistAcct item
   Description: Calls GetByID to retrieve the AlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   */  
export function get_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistAcct for the service
   Description: Calls UpdateExt to update AlcHistAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistAcct item
   Description: Call UpdateExt to delete AlcHistAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistActCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistActCats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistActCatRow
   */  
export function get_AlcHistActCats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistActCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistActCats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats", {
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
   Summary: Calls GetByID to retrieve the AlcHistActCat item
   Description: Calls GetByID to retrieve the AlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistActCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   */  
export function get_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistActCat for the service
   Description: Calls UpdateExt to update AlcHistActCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistActCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistActCat item
   Description: Call UpdateExt to delete AlcHistActCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistActCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistDtlRow
   */  
export function get_AlcHistDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls", {
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
   Summary: Calls GetByID to retrieve the AlcHistDtl item
   Description: Calls GetByID to retrieve the AlcHistDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   */  
export function get_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistDtl for the service
   Description: Calls UpdateExt to update AlcHistDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistDtl item
   Description: Call UpdateExt to delete AlcHistDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistJrnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistJrnCds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistJrnCdRow
   */  
export function get_AlcHistJrnCds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistJrnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistJrnCds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds", {
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
   Summary: Calls GetByID to retrieve the AlcHistJrnCd item
   Description: Calls GetByID to retrieve the AlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   */  
export function get_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistJrnCd for the service
   Description: Calls UpdateExt to update AlcHistJrnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistJrnCd item
   Description: Call UpdateExt to delete AlcHistJrnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistParams
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsRow
   */  
export function get_AlcHistParams(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams", {
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
   Summary: Calls GetByID to retrieve the AlcHistParam item
   Description: Calls GetByID to retrieve the AlcHistParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistParam for the service
   Description: Calls UpdateExt to update AlcHistParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistParam item
   Description: Call UpdateExt to delete AlcHistParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistParamsBAQs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistParamsBAQs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsBAQRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistParamsBAQs(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistParamsBAQs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistParamsBAQ item
   Description: Calls GetByID to retrieve the AlcHistParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParamsBAQ1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get AlcHistNFSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistNFSrcs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistNFSrcRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistNFSrcs(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistNFSrcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AlcHistNFSrc item
   Description: Calls GetByID to retrieve the AlcHistNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistNFSrc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistAccts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistAcctRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistAccts(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PAlcHistAcct item
   Description: Calls GetByID to retrieve the PAlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistAcct1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistActCats items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistActCats1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistActCatRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistActCats(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistActCats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PAlcHistActCat item
   Description: Calls GetByID to retrieve the PAlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistActCat1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistJrnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistJrnCds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistJrnCdRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistJrnCds(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistJrnCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PAlcHistJrnCd item
   Description: Calls GetByID to retrieve the PAlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistJrnCd1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistRanges items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistRanges1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistRangeRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistRanges(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistRanges", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PAlcHistRange item
   Description: Calls GetByID to retrieve the PAlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistRange1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   */  
export function get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistParamsBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistParamsBAQs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsBAQRow
   */  
export function get_AlcHistParamsBAQs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistParamsBAQs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistParamsBAQs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs", {
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
   Summary: Calls GetByID to retrieve the AlcHistParamsBAQ item
   Description: Calls GetByID to retrieve the AlcHistParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParamsBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   */  
export function get_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistParamsBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistParamsBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistParamsBAQ for the service
   Description: Calls UpdateExt to update AlcHistParamsBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistParamsBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistParamsBAQ item
   Description: Call UpdateExt to delete AlcHistParamsBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistParamsBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param BAQExportID Desc: BAQExportID   Required: True   Allow empty value : True
      @param BAQParamValNbr Desc: BAQParamValNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, BAQExportID:string, BAQParamValNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistNFSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistNFSrcs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistNFSrcRow
   */  
export function get_AlcHistNFSrcs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistNFSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistNFSrcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs", {
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
   Summary: Calls GetByID to retrieve the AlcHistNFSrc item
   Description: Calls GetByID to retrieve the AlcHistNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistNFSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   */  
export function get_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistNFSrcRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistNFSrcRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistNFSrc for the service
   Description: Calls UpdateExt to update AlcHistNFSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistNFSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistNFSrc item
   Description: Call UpdateExt to delete AlcHistNFSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistNFSrc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SrcSeqNbr Desc: SrcSeqNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SrcSeqNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistAcctRow
   */  
export function get_PAlcHistAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PAlcHistAccts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts", {
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
   Summary: Calls GetByID to retrieve the PAlcHistAcct item
   Description: Calls GetByID to retrieve the PAlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   */  
export function get_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PAlcHistAcct for the service
   Description: Calls UpdateExt to update PAlcHistAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PAlcHistAcct item
   Description: Call UpdateExt to delete PAlcHistAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param AllocGLAcct Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, AllocGLAcct:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistActCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistActCats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistActCatRow
   */  
export function get_PAlcHistActCats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistActCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PAlcHistActCats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats", {
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
   Summary: Calls GetByID to retrieve the PAlcHistActCat item
   Description: Calls GetByID to retrieve the PAlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistActCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   */  
export function get_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistActCatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistActCatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PAlcHistActCat for the service
   Description: Calls UpdateExt to update PAlcHistActCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistActCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PAlcHistActCat item
   Description: Call UpdateExt to delete PAlcHistActCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistActCat
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param CategoryID Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, CategoryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistJrnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistJrnCds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistJrnCdRow
   */  
export function get_PAlcHistJrnCds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistJrnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PAlcHistJrnCds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds", {
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
   Summary: Calls GetByID to retrieve the PAlcHistJrnCd item
   Description: Calls GetByID to retrieve the PAlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   */  
export function get_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistJrnCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistJrnCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PAlcHistJrnCd for the service
   Description: Calls UpdateExt to update PAlcHistJrnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PAlcHistJrnCd item
   Description: Call UpdateExt to delete PAlcHistJrnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistJrnCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param JournalCode Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, JournalCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistRanges
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistRangeRow
   */  
export function get_PAlcHistRanges(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PAlcHistRanges(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges", {
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
   Summary: Calls GetByID to retrieve the PAlcHistRange item
   Description: Calls GetByID to retrieve the PAlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   */  
export function get_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PAlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PAlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PAlcHistRange for the service
   Description: Calls UpdateExt to update PAlcHistRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete PAlcHistRange item
   Description: Call UpdateExt to delete PAlcHistRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistRanges
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistRangeRow
   */  
export function get_AlcHistRanges(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistRanges(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges", {
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
   Summary: Calls GetByID to retrieve the AlcHistRange item
   Description: Calls GetByID to retrieve the AlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   */  
export function get_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistRangeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistRangeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistRange for the service
   Description: Calls UpdateExt to update AlcHistRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistRange item
   Description: Call UpdateExt to delete AlcHistRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistRange
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, ParamNbr:string, SegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistResParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistResParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistResParamsRow
   */  
export function get_AlcHistResParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistResParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistResParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams", {
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
   Summary: Calls GetByID to retrieve the AlcHistResParam item
   Description: Calls GetByID to retrieve the AlcHistResParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistResParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
   */  
export function get_AlcHistResParams_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, ParamNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistResParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistResParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistResParam for the service
   Description: Calls UpdateExt to update AlcHistResParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistResParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistResParams_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, ParamNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistResParam item
   Description: Call UpdateExt to delete AlcHistResParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistResParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistResParams_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, ParamNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get AlcHistResParamsSims items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistResParamsSims
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistResParamsSimRow
   */  
export function get_AlcHistResParamsSims(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistResParamsSims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHistResParamsSims(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims", {
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
   Summary: Calls GetByID to retrieve the AlcHistResParamsSim item
   Description: Calls GetByID to retrieve the AlcHistResParamsSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistResParamsSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param ParamNbr Desc: ParamNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
   */  
export function get_AlcHistResParamsSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, ParamNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHistResParamsSimRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHistResParamsSimRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHistResParamsSim for the service
   Description: Calls UpdateExt to update AlcHistResParamsSim. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistResParamsSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHistResParamsSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, ParamNbr:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete AlcHistResParamsSim item
   Description: Call UpdateExt to delete AlcHistResParamsSim item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistResParamsSim
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BatchID Desc: BatchID   Required: True   Allow empty value : True
      @param RunNbr Desc: RunNbr   Required: True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param AllocTgtNbr Desc: AllocTgtNbr   Required: True
      @param AllocTgtSeq Desc: AllocTgtSeq   Required: True
      @param ParamNbr Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHistResParamsSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company:string, BatchID:string, RunNbr:string, AllocID:string, AllocTgtNbr:string, AllocTgtSeq:string, ParamNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", {
          method: 'delete',
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseAlcHist:string, whereClauseAHGLJrnDtl:string, whereClauseAlcHistResParams:string, whereClauseAHGLJrnDtlSim:string, whereClauseAlcHistResParamsSim:string, whereClauseAlcHistAcct:string, whereClauseAlcHistActCat:string, whereClauseAlcHistDtl:string, whereClauseAlcHistJrnCd:string, whereClauseAlcHistParams:string, whereClauseAlcHistParamsBAQ:string, whereClauseAlcHistNFSrc:string, whereClausePAlcHistAcct:string, whereClausePAlcHistActCat:string, whereClausePAlcHistJrnCd:string, whereClausePAlcHistRange:string, whereClauseAlcHistRange:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAlcHist!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHist=" + whereClauseAlcHist
   }
   if(typeof whereClauseAHGLJrnDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAHGLJrnDtl=" + whereClauseAHGLJrnDtl
   }
   if(typeof whereClauseAlcHistResParams!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistResParams=" + whereClauseAlcHistResParams
   }
   if(typeof whereClauseAHGLJrnDtlSim!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAHGLJrnDtlSim=" + whereClauseAHGLJrnDtlSim
   }
   if(typeof whereClauseAlcHistResParamsSim!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistResParamsSim=" + whereClauseAlcHistResParamsSim
   }
   if(typeof whereClauseAlcHistAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistAcct=" + whereClauseAlcHistAcct
   }
   if(typeof whereClauseAlcHistActCat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistActCat=" + whereClauseAlcHistActCat
   }
   if(typeof whereClauseAlcHistDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistDtl=" + whereClauseAlcHistDtl
   }
   if(typeof whereClauseAlcHistJrnCd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistJrnCd=" + whereClauseAlcHistJrnCd
   }
   if(typeof whereClauseAlcHistParams!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistParams=" + whereClauseAlcHistParams
   }
   if(typeof whereClauseAlcHistParamsBAQ!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistParamsBAQ=" + whereClauseAlcHistParamsBAQ
   }
   if(typeof whereClauseAlcHistNFSrc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistNFSrc=" + whereClauseAlcHistNFSrc
   }
   if(typeof whereClausePAlcHistAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePAlcHistAcct=" + whereClausePAlcHistAcct
   }
   if(typeof whereClausePAlcHistActCat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePAlcHistActCat=" + whereClausePAlcHistActCat
   }
   if(typeof whereClausePAlcHistJrnCd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePAlcHistJrnCd=" + whereClausePAlcHistJrnCd
   }
   if(typeof whereClausePAlcHistRange!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePAlcHistRange=" + whereClausePAlcHistRange
   }
   if(typeof whereClauseAlcHistRange!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHistRange=" + whereClauseAlcHistRange
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetRows" + params, {
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

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(batchID:string, runNbr:string, allocID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof batchID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "batchID=" + batchID
   }
   if(typeof runNbr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "runNbr=" + runNbr
   }
   if(typeof allocID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "allocID=" + allocID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetByID" + params, {
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

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetList" + params, {
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

   /**  
   Summary: Invoke method GetByBatchIDRunNbr
   Description: Wrapper method for GetRows with BatchID and RunNbr filters
   OperationID: GetByBatchIDRunNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByBatchIDRunNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByBatchIDRunNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByBatchIDRunNbr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetByBatchIDRunNbr", {
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
   Summary: Invoke method GetListByBatchID
   Description: One AlcHist record for each BatchID.  Call normal GetList method.
   OperationID: GetListByBatchID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByBatchID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByBatchID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByBatchID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetListByBatchID", {
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
   Summary: Invoke method GetNewAlcHistoryFilter
   Description: This method creates a new AlcHistoryFilter record.
   OperationID: GetNewAlcHistoryFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistoryFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistoryFilter(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistoryFilter", {
          method: 'post',
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

   /**  
   Summary: Invoke method OnChangeBookID
   Description: This method is called when the BookID is changed.
   OperationID: OnChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBookID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/OnChangeBookID", {
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
   Summary: Invoke method OnChangeFiscalYearOrSuffix
   Description: Verifies selected start\end period and updates if year doesn't contain current values.
   OperationID: OnChangeFiscalYearOrSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYearOrSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYearOrSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFiscalYearOrSuffix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/OnChangeFiscalYearOrSuffix", {
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
   Summary: Invoke method GetNewAlcHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHist", {
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
   Summary: Invoke method GetNewAHGLJrnDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAHGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAHGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAHGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAHGLJrnDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAHGLJrnDtl", {
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
   Summary: Invoke method GetNewAlcHistResParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistResParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistResParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistResParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistResParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistResParams", {
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
   Summary: Invoke method GetNewAHGLJrnDtlSim
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAHGLJrnDtlSim
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAHGLJrnDtlSim_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAHGLJrnDtlSim_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAHGLJrnDtlSim(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAHGLJrnDtlSim", {
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
   Summary: Invoke method GetNewAlcHistResParamsSim
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistResParamsSim
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistResParamsSim_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistResParamsSim_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistResParamsSim(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistResParamsSim", {
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
   Summary: Invoke method GetNewAlcHistAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistAcct", {
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
   Summary: Invoke method GetNewAlcHistActCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistActCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistActCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistActCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistActCat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistActCat", {
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
   Summary: Invoke method GetNewAlcHistDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistDtl", {
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
   Summary: Invoke method GetNewAlcHistJrnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistJrnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistJrnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistJrnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistJrnCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistJrnCd", {
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
   Summary: Invoke method GetNewAlcHistParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistParams", {
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
   Summary: Invoke method GetNewAlcHistParamsBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistParamsBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistParamsBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistParamsBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistParamsBAQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistParamsBAQ", {
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
   Summary: Invoke method GetNewAlcHistNFSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistNFSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistNFSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistNFSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistNFSrc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistNFSrc", {
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
   Summary: Invoke method GetNewPAlcHistAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPAlcHistAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewPAlcHistAcct", {
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
   Summary: Invoke method GetNewPAlcHistActCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistActCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistActCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistActCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPAlcHistActCat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewPAlcHistActCat", {
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
   Summary: Invoke method GetNewPAlcHistJrnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistJrnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistJrnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistJrnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPAlcHistJrnCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewPAlcHistJrnCd", {
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
   Summary: Invoke method GetNewPAlcHistRange
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPAlcHistRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewPAlcHistRange", {
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
   Summary: Invoke method GetNewAlcHistRange
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHistRange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetNewAlcHistRange", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetBySysRowID" + params, {
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

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/GetBySysRowIDs" + params, {
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

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AHGLJrnDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlSimRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AHGLJrnDtlSimRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistAcctRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistActCatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistActCatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistJrnCdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistJrnCdRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistNFSrcRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistNFSrcRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsBAQRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistParamsBAQRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistParamsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRangeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistRangeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistResParamsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsSimRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistResParamsSimRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHistRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PAlcHistAcctRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistActCatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PAlcHistActCatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistJrnCdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PAlcHistJrnCdRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistRangeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PAlcHistRangeRow[],
}

export interface Erp_Tablesets_AHGLJrnDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   "Description":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  User ID that posted this translation.  */  
   "PostedBy":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   "Posted":boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   "SourceModule":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "ARInvoiceNum":number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   "BankAcctID":string,
      /**  Check number.  */  
   "CheckNum":number,
      /**  Cash Receipts reference field.  */  
   "CRHeadNum":number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   "Reverse":boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   "BankTranNum":number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   "BankSlip":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefType":string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefCode":string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalNum":number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalLine":number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   "GlbJournalCode":string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   "GlbVendorNum":number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   "GlbAPInvoiceNum":string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   "MultiCompany":boolean,
      /**  Linked to a Multi-Company Journal.  */  
   "Linked":boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   "CommentText":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "GlbCompanyID":string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   "GlbFiscalYear":number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   "GlbFiscalPeriod":number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   "GlbGroupID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAccount":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "ExtGLAccount":string,
      /**  External Segment Value 1  */  
   "ExtSegValue1":string,
      /**  External Segment Value 2  */  
   "ExtSegValue2":string,
      /**  External Segment Value 3  */  
   "ExtSegValue3":string,
      /**  External Segment Value 4  */  
   "ExtSegValue4":string,
      /**  External Segment Value 5  */  
   "ExtSegValue5":string,
      /**  External Segment Value 6  */  
   "ExtSegValue6":string,
      /**  External Segment Value 7  */  
   "ExtSegValue7":string,
      /**  External Segment Value 8  */  
   "ExtSegValue8":string,
      /**  External Segment Value 9  */  
   "ExtSegValue9":string,
      /**  External Segment Value 10  */  
   "ExtSegValue10":string,
      /**  External Segment Value 11  */  
   "ExtSegValue11":string,
      /**  External Segment Value 12  */  
   "ExtSegValue12":string,
      /**  External Segment Value 13  */  
   "ExtSegValue13":string,
      /**  External Segment Value 14  */  
   "ExtSegValue14":string,
      /**  External Segment Value 15  */  
   "ExtSegValue15":string,
      /**  External Segment Value 16  */  
   "ExtSegValue16":string,
      /**  External Segment Value 17  */  
   "ExtSegValue17":string,
      /**  External Segment Value 18  */  
   "ExtSegValue18":string,
      /**  External Segment Value 19  */  
   "ExtSegValue19":string,
      /**  External Segment Value 20  */  
   "ExtSegValue20":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**  Legal Number of source document  */  
   "LegalNumber":string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "PerBalFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "TBFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "DailyBalFlag":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year suffix.  */  
   "GlbFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "GlbFiscalCalendarID":string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   "IntermediateProc":boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   "SrcCompany":string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SrcBook":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "SrcGLAccount":string,
      /**  Source Journal Code  */  
   "SrcJrnlCode":string,
      /**  Source Journal Number  */  
   "SrcJournalNum":number,
      /**  Source Journal Line  */  
   "SrcJournalLine":number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   "SrcType":string,
      /**  this field equas ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  This field shows Debit value of transaction  */  
   "DebitAmount":number,
      /**  This field shows Credit value of transaction  */  
   "CreditAmount":number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   "BookDebitAmount":number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   "BookCreditAmount":number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   "ParentRUID":string,
      /**  if has reverse line  */  
   "HasReverseLine":boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   "BalanceAcct":string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   "TrialAcct":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   "AllocationStamp":string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   "BatchID":string,
      /**  This is the allocation id that processed this journal entry.  */  
   "AllocID":string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   "RunNbr":number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   "AllocRunNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtSeq":number,
      /**  External COA Code  */  
   "ExtCOACode":string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   "MatchCode":string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   "MatchDate":string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   "Reconciled":boolean,
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
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Journal Sequence Number  */  
   "Sequence":number,
      /**  Transaction Document Type  */  
   "TranDocTypeID":string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   "CustNum":number,
      /**  CloseFiscalPeriod  */  
   "CloseFiscalPeriod":number,
      /**  SourcePlant  */  
   "SourcePlant":string,
      /**  Plant  */  
   "Plant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
   "StatAmount":number,
   "BitFlag":number,
   "AHGLJrnDtlAlcHedTier":number,
   "StatUOMStatUOMDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AHGLJrnDtlSimRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   "Description":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  User ID that posted this translation.  */  
   "PostedBy":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   "Posted":boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   "SourceModule":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "ARInvoiceNum":number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   "BankAcctID":string,
      /**  Check number.  */  
   "CheckNum":number,
      /**  Cash Receipts reference field.  */  
   "CRHeadNum":number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   "Reverse":boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   "BankTranNum":number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   "BankSlip":string,
      /**  Link to the related GLRefTyp.RefType.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefType":string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   "ExtRefCode":string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalNum":number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   "GlbJournalLine":number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   "GlbJournalCode":string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   "GlbVendorNum":number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   "GlbAPInvoiceNum":string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   "MultiCompany":boolean,
      /**  Linked to a Multi-Company Journal.  */  
   "Linked":boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   "CommentText":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "GlbCompanyID":string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   "GlbFiscalYear":number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   "GlbFiscalPeriod":number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   "GlbGroupID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "GLAccount":string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SegValue1":string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SegValue2":string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SegValue3":string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SegValue4":string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SegValue5":string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SegValue6":string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SegValue7":string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SegValue8":string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SegValue9":string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SegValue10":string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SegValue11":string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SegValue12":string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SegValue13":string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SegValue14":string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SegValue15":string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SegValue16":string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SegValue17":string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SegValue18":string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SegValue19":string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SegValue20":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "ExtGLAccount":string,
      /**  External Segment Value 1  */  
   "ExtSegValue1":string,
      /**  External Segment Value 2  */  
   "ExtSegValue2":string,
      /**  External Segment Value 3  */  
   "ExtSegValue3":string,
      /**  External Segment Value 4  */  
   "ExtSegValue4":string,
      /**  External Segment Value 5  */  
   "ExtSegValue5":string,
      /**  External Segment Value 6  */  
   "ExtSegValue6":string,
      /**  External Segment Value 7  */  
   "ExtSegValue7":string,
      /**  External Segment Value 8  */  
   "ExtSegValue8":string,
      /**  External Segment Value 9  */  
   "ExtSegValue9":string,
      /**  External Segment Value 10  */  
   "ExtSegValue10":string,
      /**  External Segment Value 11  */  
   "ExtSegValue11":string,
      /**  External Segment Value 12  */  
   "ExtSegValue12":string,
      /**  External Segment Value 13  */  
   "ExtSegValue13":string,
      /**  External Segment Value 14  */  
   "ExtSegValue14":string,
      /**  External Segment Value 15  */  
   "ExtSegValue15":string,
      /**  External Segment Value 16  */  
   "ExtSegValue16":string,
      /**  External Segment Value 17  */  
   "ExtSegValue17":string,
      /**  External Segment Value 18  */  
   "ExtSegValue18":string,
      /**  External Segment Value 19  */  
   "ExtSegValue19":string,
      /**  External Segment Value 20  */  
   "ExtSegValue20":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**  Legal Number of source document  */  
   "LegalNumber":string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "SummaryBalFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "DetailBalFlag":boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   "DailyBalFlag":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Fiscal year suffix.  */  
   "GlbFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "GlbFiscalCalendarID":string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   "IntermediateProc":boolean,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   "GenID":number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   "SrcCompany":string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   "SrcBook":string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   "SrcGLAccount":string,
      /**  Source Journal Code  */  
   "SrcJrnlCode":string,
      /**  Source Journal Number  */  
   "SrcJournalNum":number,
      /**  Source Journal Line  */  
   "SrcJournalLine":number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  */  
   "SrcType":string,
      /**  this field equas ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  This field shows Debit value of transaction  */  
   "DebitAmount":number,
      /**  This field shows Credit value of transaction  */  
   "CreditAmount":number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   "BookDebitAmount":number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   "BookCreditAmount":number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   "ParentRUID":string,
      /**  if has reverse line  */  
   "HasReverseLine":boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   "BalanceAcct":string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   "SummaryAcct":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  This is the allocation stamp that processed this journal entry.  Allocation Marks are entered on an Allocation Code.  */  
   "AllocationStamp":string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   "BatchID":string,
      /**  This is the allocation id that processed this journal entry.  */  
   "AllocID":string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was processed under.  */  
   "RunNbr":number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   "AllocRunNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtSeq":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   "CustNum":number,
   "StatAmount":number,
   "BitFlag":number,
   "AHGLJrnDtlSimAlcHedTier":number,
   "StatUOMStatUOMDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  GL Account or GL Account mask  */  
   "AllocGLAcct":string,
      /**  Allocation Segment Value 1  */  
   "AllocSegValue1":string,
      /**  Allocation Segment Value 2  */  
   "AllocSegValue2":string,
      /**  Allocation Segment Value 3  */  
   "AllocSegValue3":string,
      /**  Allocation Segment Value 4  */  
   "AllocSegValue4":string,
      /**  Allocation Segment Value 5  */  
   "AllocSegValue5":string,
      /**  Allocation Segment Value 6  */  
   "AllocSegValue6":string,
      /**  Allocation Segment Value 7  */  
   "AllocSegValue7":string,
      /**  Allocation Segment Value 8  */  
   "AllocSegValue8":string,
      /**  Allocation Segment Value 9  */  
   "AllocSegValue9":string,
      /**  Allocation Segment Value 10  */  
   "AllocSegValue10":string,
      /**  Allocation Segment Value 11  */  
   "AllocSegValue11":string,
      /**  Allocation Segment Value 12  */  
   "AllocSegValue12":string,
      /**  Allocation Segment Value 13  */  
   "AllocSegValue13":string,
      /**  Allocation Segment Value 14  */  
   "AllocSegValue14":string,
      /**  Allocation Segment Value 15  */  
   "AllocSegValue15":string,
      /**  Allocation Segment Value 16  */  
   "AllocSegValue16":string,
      /**  Allocation Segment Value 17  */  
   "AllocSegValue17":string,
      /**  Allocation Segment Value 18  */  
   "AllocSegValue18":string,
      /**  Allocation Segment Value 19  */  
   "AllocSegValue19":string,
      /**  Allocation Segment Value 20  */  
   "AllocSegValue20":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "AllocGLAcctGLShortAcct":string,
   "AllocGLAcctAccountDesc":string,
   "AllocGLAcctGLAcctDisp":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistActCatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique identifier of this category of accounts.  */  
   "CategoryID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtSeq":number,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   "JournalNum":number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   "JournalLine":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Yes indicates this record contains information about the amount written off against the source account.  NO indicates this record contains information about the amount allocated.  */  
   "WriteOff":boolean,
      /**  Initial balance of the write off account.  Only updated when WriteOff = yes.  */  
   "SourceInitBalance":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Source GL Account or Balance Account.  */  
   "SourceAccount":string,
      /**  Account the source amount was allocated to.  */  
   "TargetAccount":string,
      /**  REsolved GL Account.  This is the same as the target account if the target account does not have any mask characters.  */  
   "ResolvedAccount":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  */  
   "AllocUnits":number,
      /**  Postive, fractional value indicating how much of an allocation is applied to this target.  */  
   "RatioValue":number,
      /**  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  */  
   "RatioFormula":string,
      /**  Resolved Formula based upon the Ratio Formula.  Only valid if the allocation option = 2.  */  
   "ResolvedFormula":string,
      /**  Yes indicates this entry is a reversing entry.  No indicates it is not a reversing entry.  */  
   "ReversingEntry":boolean,
      /**  Target Segment Value 1  */  
   "TgtSegVal1":string,
      /**  Target Segment Value 2  */  
   "TgtSegVal2":string,
      /**  Target Segment Value 3  */  
   "TgtSegVal3":string,
      /**  Target Segment Value 4  */  
   "TgtSegVal4":string,
      /**  Target Segment Value 5  */  
   "TgtSegVal5":string,
      /**  Target Segment Value 6  */  
   "TgtSegVal6":string,
      /**  Target Segment Value 7  */  
   "TgtSegVal7":string,
      /**  Target Segment Value 8  */  
   "TgtSegVal8":string,
      /**  Target Segment Value 9  */  
   "TgtSegVal9":string,
      /**  Target Segment Value 10  */  
   "TgtSegVal10":string,
      /**  Target Segment Value 11  */  
   "TgtSegVal11":string,
      /**  Target Segment Value 12  */  
   "TgtSegVal12":string,
      /**  Target Segment Value 13  */  
   "TgtSegVal13":string,
      /**  Target Segment Value 14  */  
   "TgtSegVal14":string,
      /**  Target Segment Value 15  */  
   "TgtSegVal15":string,
      /**  Target Segment Value 16  */  
   "TgtSegVal16":string,
      /**  Target Segment Value 17  */  
   "TgtSegVal17":string,
      /**  Target Segment Value 18  */  
   "TgtSegVal18":string,
      /**  Target Segment Value 19  */  
   "TgtSegVal19":string,
      /**  Target Segment Value 20  */  
   "TgtSegVal20":string,
      /**  Source Segment Value 1  */  
   "SrcSegVal1":string,
      /**  Source Segment Value 2  */  
   "SrcSegVal2":string,
      /**  Source Segment Value 3  */  
   "SrcSegVal3":string,
      /**  Source Segment Value 4  */  
   "SrcSegVal4":string,
      /**  Source Segment Value 5  */  
   "SrcSegVal5":string,
      /**  Source Segment Value 6  */  
   "SrcSegVal6":string,
      /**  Source Segment Value 7  */  
   "SrcSegVal7":string,
      /**  Source Segment Value 8  */  
   "SrcSegVal8":string,
      /**  Source Segment Value 9  */  
   "SrcSegVal9":string,
      /**  Source Segment Value 10  */  
   "SrcSegVal10":string,
      /**  Source Segment Value 11  */  
   "SrcSegVal11":string,
      /**  Source Segment Value 12  */  
   "SrcSegVal12":string,
      /**  Source Segment Value 13  */  
   "SrcSegVal13":string,
      /**  Source Segment Value 14  */  
   "SrcSegVal14":string,
      /**  Source Segment Value 15  */  
   "SrcSegVal15":string,
      /**  Source Segment Value 16  */  
   "SrcSegVal16":string,
      /**  Source Segment Value 17  */  
   "SrcSegVal17":string,
      /**  Source Segment Value 18  */  
   "SrcSegVal18":string,
      /**  Source Segment Value 19  */  
   "SrcSegVal19":string,
      /**  Source Segment Value 20  */  
   "SrcSegVal20":string,
      /**  Resolved Segment Value 1  */  
   "ResSegVal1":string,
      /**  Resolved Segment Value 2  */  
   "ResSegVal2":string,
      /**  Resolved Segment Value 3  */  
   "ResSegVal3":string,
      /**  Resolved Segment Value 4  */  
   "ResSegVal4":string,
      /**  Resolved Segment Value 5  */  
   "ResSegVal5":string,
      /**  Resolved Segment Value 6  */  
   "ResSegVal6":string,
      /**  Resolved Segment Value 7  */  
   "ResSegVal7":string,
      /**  Resolved Segment Value 8  */  
   "ResSegVal8":string,
      /**  Resolved Segment Value 9  */  
   "ResSegVal9":string,
      /**  Resolved Segment Value 10  */  
   "ResSegVal10":string,
      /**  Resolved Segment Value 11  */  
   "ResSegVal11":string,
      /**  Resolved Segment Value 12  */  
   "ResSegVal12":string,
      /**  Resolved Segment Value 13  */  
   "ResSegVal13":string,
      /**  Resolved Segment Value 14  */  
   "ResSegVal14":string,
      /**  Resolved Segment Value 15  */  
   "ResSegVal15":string,
      /**  Resolved Segment Value 16  */  
   "ResSegVal16":string,
      /**  Resolved Segment Value 17  */  
   "ResSegVal17":string,
      /**  Resolved Segment Value 18  */  
   "ResSegVal18":string,
      /**  Resolved Segment Value 19  */  
   "ResSegVal19":string,
      /**  Resolved Segment Value 20  */  
   "ResSegVal20":string,
      /**  The reversed fiscal year.  This is updated by reverse allocation run logic.  */  
   "ReverseFY":number,
      /**   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated by reverse allocation run logic.  */  
   "ReverseFYS":string,
      /**   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated by reverse allocation run logic.  */  
   "ReverseJournalNum":number,
      /**   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a
.specific Company/FiscalYear/JournalNum combination and adding 1.This is updated by reverse allocation run logic  */  
   "ReverseJournalLine":number,
      /**  Source amount applied to the formula/percentage during an allocation.  */  
   "SrcDebitAmount":number,
      /**  Source amount applied to the formula/percentage during an allocation.  */  
   "SrcCreditAmount":number,
      /**  The reversed entry fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   "RevEntryFY":number,
      /**   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   "RevEntryFYS":string,
      /**   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   "RevEntryJrnlNum":number,
      /**   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   "RevEntryJrnlLine":number,
      /**  The reversed entry reversing fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and the reversing journal entry is reversed.  */  
   "RevReverseFY":number,
      /**   The reversed reversing entry fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  */  
   "RevReverseFYS":string,
      /**   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  */  
   "RevReverseJrnlNum":number,
      /**   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  */  
   "RevReverseJrnlLine":number,
      /**  Cycle unique ID.  This is not intended for external use.  */  
   "CycleUID":number,
      /**  Cycle number.  */  
   "CycleNumber":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "GLAccount":string,
   "CreditAmount":number,
   "DebitAmount":number,
   "JEDate":string,
   "BitFlag":number,
   "AlcHistDtlAlcHedTier":number,
   "AlcHistDtlJrnlCdJrnlDescription":string,
   "ResolvedGLAcctDispGLShortAcct":string,
   "ResolvedGLAcctDispGLAcctDisp":string,
   "ResolvedGLAcctDispAccountDesc":string,
   "SourceAccountAccountDesc":string,
   "SourceAccountGLShortAcct":string,
   "SourceAccountGLAcctDisp":string,
   "TargetAccountAccountDesc":string,
   "TargetAccountGLShortAcct":string,
   "TargetAccountGLAcctDisp":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistJrnCdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   "JournalCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "JrnlCodeJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Date the batch was run.  */  
   "RunDate":string,
      /**  Time the allocaiton batch run started.  */  
   "RunTime":number,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  User ID  */  
   "DcdUserID":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Indicates if this is simulation history record or General Ledger history record.  */  
   "Simulation":boolean,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Apply Date for journal transactions.  */  
   "ApplyDate":string,
      /**  Date used for reversing entries.  */  
   "ApplyDateRev":string,
      /**  Starting date for record selection.  Defaults to the fiscal period start date.  */  
   "StartDate":string,
      /**  Ending date for record seletion.  Defaults to fiscal period end date.  */  
   "EndDate":string,
      /**  Date when the allocation batch is due to be run.  */  
   "SchedDate":string,
      /**  Batch Description  */  
   "BatchDesc":string,
      /**  Allocation tier.  */  
   "Tier":number,
      /**  Internal next number used to keep the schedule records unique.  */  
   "SchedNum":number,
      /**  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  */  
   "Reverse":boolean,
      /**  Indicates if the allocation run started at the beginning of the current fiscal year.  */  
   "YTDAlloc":boolean,
      /**  Indicates if the allocation run has been reversed.  */  
   "AllocReversed":boolean,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   "PriorTgtStamp":string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   "TgtStamp":string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   "SrcAllocStamp":string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   "IgnoreStamp":boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   "UseAllStamps":boolean,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   "PercentToAlloc":number,
      /**  Indicates if the allocation units are used.  */  
   "UseAllocUnits":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RunTypeDesc":string,
      /**  Calendar description.  */  
   "AlcHistFiscalCalDescription":string,
      /**  Indicates the base currency for the book  */  
   "AlcHistGLBookCurrencyCode":string,
      /**  Descripiton of Book  */  
   "AlcHistGLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistNFSrcRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. The value of ParamNbr identifies the parameter number the record is defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  LookupTblMapUID_obsolete  */  
   "LookupTblMapUID_obsolete":number,
      /**  TgtSeqNbr_obsolete  */  
   "TgtSeqNbr_obsolete":number,
      /**  LinkUID_obsolete  */  
   "LinkUID_obsolete":number,
      /**  Source field name.  */  
   "SrcFieldName":string,
      /**   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   "ParamOpt":number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   "ParamSegmentNbr":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   "EntryType":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SrcSeqNbr  */  
   "SrcSeqNbr":number,
      /**  SrcCodeID  */  
   "SrcCodeID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistParamsBAQRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Intended for internal use only to keep the records unique.  */  
   "ParamNbr":number,
      /**  BAQ ID, the unique identifier for this Query table within the company  */  
   "BAQExportID":string,
      /**  Intended for internal use only to keep the records unique.  */  
   "BAQParamValNbr":number,
   "ParameterName":string,
      /**  Specific baq parameter value.  */  
   "BAQParamCode":string,
      /**   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   "ParamOpt":number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   "ParamSegmentNbr":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   "EntryType":number,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistParamsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  The name assigned to a parameter.  This name must be unique.  */  
   "ParamName":string,
      /**  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances and 3 = BAQ.  */  
   "ParamType":number,
      /**  Text that describes the parameter.  */  
   "ParamDesc":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Account balance account.  Only valid when the formula type = 1.  */  
   "AcctBalAcct":string,
      /**  Account Segment Value 1  */  
   "AcctBalSegVal1":string,
      /**  Account Segment Value 2  */  
   "AcctBalSegVal2":string,
      /**  Account Segment Value 3  */  
   "AcctBalSegVal3":string,
      /**  Account Segment Value 4  */  
   "AcctBalSegVal4":string,
      /**  Account Segment Value 5  */  
   "AcctBalSegVal5":string,
      /**  Account Segment Value 6  */  
   "AcctBalSegVal6":string,
      /**  Account Segment Value 7  */  
   "AcctBalSegVal7":string,
      /**  Account Segment Value 8  */  
   "AcctBalSegVal8":string,
      /**  Account Segment Value 9  */  
   "AcctBalSegVal9":string,
      /**  Account Segment Value 10  */  
   "AcctBalSegVal10":string,
      /**  Account Segment Value 11  */  
   "AcctBalSegVal11":string,
      /**  Account Segment Value 12  */  
   "AcctBalSegVal12":string,
      /**  Account Segment Value 13  */  
   "AcctBalSegVal13":string,
      /**  Account Segment Value 14  */  
   "AcctBalSegVal14":string,
      /**  Account Segment Value 15  */  
   "AcctBalSegVal15":string,
      /**  Account Segment Value 16  */  
   "AcctBalSegVal16":string,
      /**  Account Segment Value 17  */  
   "AcctBalSegVal17":string,
      /**  Account Segment Value 18  */  
   "AcctBalSegVal18":string,
      /**  Account Segment Value 19  */  
   "AcctBalSegVal19":string,
      /**  Account Segment Value 20  */  
   "AcctBalSegVal20":string,
      /**  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  */  
   "UseTgtAcct":boolean,
      /**  BAQ  ID, the unique identifier for the query table within the company  */  
   "BAQExportID":string,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  */  
   "AcctParamValSrc":number,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  */  
   "SumParamValSrc":number,
      /**  Indicates if the allocation run was reversed.  */  
   "Reversed":boolean,
      /**  Date used to reverse the allocation run.  */  
   "ReversedDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NFSrcMapUID  */  
   "NFSrcMapUID":number,
      /**  NFTgtSeqNbr  */  
   "NFTgtSeqNbr":number,
      /**  YTDBalance  */  
   "YTDBalance":boolean,
   "BitFlag":number,
   "AcctBalAcctGLAcctDispAccountDesc":string,
   "AcctBalAcctGLAcctDispGLShortAcct":string,
   "AcctBalAcctGLAcctDispGLAcctDisp":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistRangeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Minimum vale for range selection.  */  
   "MinValue":string,
      /**  Maximum value for range selection.  */  
   "MaxValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "COASegmentSegmentName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistResParamsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtSeq":number,
      /**  Intended for internal use only to keep the records unique.  */  
   "ParamNbr":number,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Actual calculated value.  */  
   "ActualValue":number,
      /**  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  */  
   "ResBalAcct":string,
      /**  Resolved  Segment Value 1  */  
   "ResBalSegVal1":string,
      /**  Resolved  Segment Value 2  */  
   "ResBalSegVal2":string,
      /**  Resolved  Segment Value 3  */  
   "ResBalSegVal3":string,
      /**  Resolved Segment Value 4  */  
   "ResBalSegVal4":string,
      /**  Resolved  Segment Value 5  */  
   "ResBalSegVal5":string,
      /**  Resolved  Segment Value 6  */  
   "ResBalSegVal6":string,
      /**  Resolved Segment Value 7  */  
   "ResBalSegVal7":string,
      /**  Resolved  Segment Value 8  */  
   "ResBalSegVal8":string,
      /**  Resolved  Segment Value 9  */  
   "ResBalSegVal9":string,
      /**  Resolved Segment Value 10  */  
   "ResBalSegVal10":string,
      /**  Resolved Segment Value 11  */  
   "ResBalSegVal11":string,
      /**  Resolved  Segment Value 12  */  
   "ResBalSegVal12":string,
      /**  Resolved  Segment Value 13  */  
   "ResBalSegVal13":string,
      /**  Resolved  Segment Value 14  */  
   "ResBalSegVal14":string,
      /**  Resolved Segment Value 15  */  
   "ResBalSegVal15":string,
      /**  Resolved  Segment Value 16  */  
   "ResBalSegVal16":string,
      /**  Resolved  Segment Value 17  */  
   "ResBalSegVal17":string,
      /**  Resolved  Segment Value 18  */  
   "ResBalSegVal18":string,
      /**  Resolved Segment Value 19  */  
   "ResBalSegVal19":string,
      /**  Resolved  Segment Value 20  */  
   "ResBalSegVal20":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Cycle unique ID.  This is not intended for external use.  */  
   "CycleUID":number,
      /**  Cycle number.  */  
   "CycleNumber":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  YTDBalance  */  
   "YTDBalance":boolean,
   "AcctBalAcct":string,
   "UseTgtAcct":boolean,
   "BAQExportID":string,
   "AcctParamValSrc":number,
   "SumParamValSrc":number,
   "TgtGLAcct":string,
   "BitFlag":number,
   "AlcHistParamsParamType":number,
   "AlcHistParamsAcctParamValSrc":number,
   "AlcHistParamsUseTgtAcct":boolean,
   "AlcHistParamsParamName":string,
   "AlcHistParamsSumParamValSrc":number,
   "AlcHistParamsBAQExportID":string,
   "AlcHistParamsAcctBalAcct":string,
   "AlcHistParamsParamDesc":string,
   "ResAcctDispGLShortAcct":string,
   "ResAcctDispGLAcctDisp":string,
   "ResAcctDispAccountDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistResParamsSimRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtNbr":number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   "AllocTgtSeq":number,
      /**  Intended for internal use only to keep the records unique.  */  
   "ParamNbr":number,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Actual calculated value.  */  
   "ActualValue":number,
      /**  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  */  
   "ResBalAcct":string,
      /**  Resolved  Segment Value 1  */  
   "ResBalSegVal1":string,
      /**  Resolved  Segment Value 2  */  
   "ResBalSegVal2":string,
      /**  Resolved  Segment Value 3  */  
   "ResBalSegVal3":string,
      /**  Resolved Segment Value 4  */  
   "ResBalSegVal4":string,
      /**  Resolved  Segment Value 5  */  
   "ResBalSegVal5":string,
      /**  Resolved  Segment Value 6  */  
   "ResBalSegVal6":string,
      /**  Resolved Segment Value 7  */  
   "ResBalSegVal7":string,
      /**  Resolved  Segment Value 8  */  
   "ResBalSegVal8":string,
      /**  Resolved  Segment Value 9  */  
   "ResBalSegVal9":string,
      /**  Resolved Segment Value 10  */  
   "ResBalSegVal10":string,
      /**  Resolved Segment Value 11  */  
   "ResBalSegVal11":string,
      /**  Resolved  Segment Value 12  */  
   "ResBalSegVal12":string,
      /**  Resolved  Segment Value 13  */  
   "ResBalSegVal13":string,
      /**  Resolved  Segment Value 14  */  
   "ResBalSegVal14":string,
      /**  Resolved Segment Value 15  */  
   "ResBalSegVal15":string,
      /**  Resolved  Segment Value 16  */  
   "ResBalSegVal16":string,
      /**  Resolved  Segment Value 17  */  
   "ResBalSegVal17":string,
      /**  Resolved  Segment Value 18  */  
   "ResBalSegVal18":string,
      /**  Resolved Segment Value 19  */  
   "ResBalSegVal19":string,
      /**  Resolved  Segment Value 20  */  
   "ResBalSegVal20":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Cycle unique ID.  This is not intended for external use.  */  
   "CycleUID":number,
      /**  Cycle number.  */  
   "CycleNumber":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  YTDBalance  */  
   "YTDBalance":boolean,
   "TgtGLAcct":string,
   "BitFlag":number,
   "AlcHistParamsSimSumParamValSrc":number,
   "AlcHistParamsSimParamName":string,
   "AlcHistParamsSimParamType":number,
   "AlcHistParamsSimAcctBalAcct":string,
   "AlcHistParamsSimParamDesc":string,
   "AlcHistParamsSimUseTgtAcct":boolean,
   "AlcHistParamsSimAcctParamValSrc":number,
   "ResAcctDispSimGLAcctDisp":string,
   "ResAcctDispSimGLShortAcct":string,
   "ResAcctDispSimAccountDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHistRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Date the batch was run.  */  
   "RunDate":string,
      /**  Time the allocaiton batch run started.  */  
   "RunTime":number,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  User ID  */  
   "DcdUserID":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Indicates if this is simulation history record or General Ledger history record.  */  
   "Simulation":boolean,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  Apply Date for journal transactions.  */  
   "ApplyDate":string,
      /**  Date used for reversing entries.  */  
   "ApplyDateRev":string,
      /**  Starting date for record selection.  Defaults to the fiscal period start date.  */  
   "StartDate":string,
      /**  Ending date for record seletion.  Defaults to fiscal period end date.  */  
   "EndDate":string,
      /**  Date when the allocation batch is due to be run.  */  
   "SchedDate":string,
      /**  Batch Description  */  
   "BatchDesc":string,
      /**  Allocation tier.  */  
   "Tier":number,
      /**  Internal next number used to keep the schedule records unique.  */  
   "SchedNum":number,
      /**  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  */  
   "Reverse":boolean,
      /**  Indicates if the allocation run started at the beginning of the current fiscal year.  */  
   "YTDAlloc":boolean,
      /**  Indicates if the allocation run has been reversed.  */  
   "AllocReversed":boolean,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   "PriorTgtStamp":string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   "TgtStamp":string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   "SrcAllocStamp":string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   "IgnoreStamp":boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   "UseAllStamps":boolean,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   "PercentToAlloc":number,
      /**  Indicates if the allocation units are used.  */  
   "UseAllocUnits":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  StatBalAsAllocUnits  */  
   "StatBalAsAllocUnits":boolean,
   "RunTypeDesc":string,
   "BitFlag":number,
   "AlcHistFiscalCalDescription":string,
   "AlcHistGLBookCurrencyCode":string,
   "AlcHistGLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PAlcHistAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  GL Account or GL Account mask  */  
   "AllocGLAcct":string,
      /**  Allocation Segment Value 1  */  
   "AllocSegValue1":string,
      /**  Allocation Segment Value 2  */  
   "AllocSegValue2":string,
      /**  Allocation Segment Value 3  */  
   "AllocSegValue3":string,
      /**  Allocation Segment Value 4  */  
   "AllocSegValue4":string,
      /**  Allocation Segment Value 5  */  
   "AllocSegValue5":string,
      /**  Allocation Segment Value 6  */  
   "AllocSegValue6":string,
      /**  Allocation Segment Value 7  */  
   "AllocSegValue7":string,
      /**  Allocation Segment Value 8  */  
   "AllocSegValue8":string,
      /**  Allocation Segment Value 9  */  
   "AllocSegValue9":string,
      /**  Allocation Segment Value 10  */  
   "AllocSegValue10":string,
      /**  Allocation Segment Value 11  */  
   "AllocSegValue11":string,
      /**  Allocation Segment Value 12  */  
   "AllocSegValue12":string,
      /**  Allocation Segment Value 13  */  
   "AllocSegValue13":string,
      /**  Allocation Segment Value 14  */  
   "AllocSegValue14":string,
      /**  Allocation Segment Value 15  */  
   "AllocSegValue15":string,
      /**  Allocation Segment Value 16  */  
   "AllocSegValue16":string,
      /**  Allocation Segment Value 17  */  
   "AllocSegValue17":string,
      /**  Allocation Segment Value 18  */  
   "AllocSegValue18":string,
      /**  Allocation Segment Value 19  */  
   "AllocSegValue19":string,
      /**  Allocation Segment Value 20  */  
   "AllocSegValue20":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PAllocGLAccountGLAcctDisp":string,
   "PAllocGLAccountGLShortAcct":string,
   "PAllocGLAccountAccountDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PAlcHistActCatRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique identifier of this category of accounts.  */  
   "CategoryID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PAlcHistJrnCdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   "JournalCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PHistJrnlCodeJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PAlcHistRangeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   "BatchID":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   "ParamNbr":number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   "RunNbr":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  1 = General Ledger, 2 = Simulation  */  
   "RunType":number,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Minimum vale for range selection.  */  
   "MinValue":string,
      /**  Maximum value for range selection.  */  
   "MaxValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PCOASegmentSegmentName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param batchID
      @param runNbr
      @param allocID
   */  
export interface DeleteByID_input{
   batchID:string,
   runNbr:number,
   allocID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AHGLJrnDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   PerBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   TBFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   SrcType:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   BalanceAcct:string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   TrialAcct:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   AllocationStamp:string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   BatchID:string,
      /**  This is the allocation id that processed this journal entry.  */  
   AllocID:string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   RunNbr:number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   AllocRunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  External COA Code  */  
   ExtCOACode:string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   MatchCode:string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   MatchDate:string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   Reconciled:boolean,
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
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  CloseFiscalPeriod  */  
   CloseFiscalPeriod:number,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Plant  */  
   Plant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
   StatAmount:number,
   BitFlag:number,
   AHGLJrnDtlAlcHedTier:number,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AHGLJrnDtlSimRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   SummaryBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DetailBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  */  
   SrcType:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   BalanceAcct:string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   SummaryAcct:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  This is the allocation stamp that processed this journal entry.  Allocation Marks are entered on an Allocation Code.  */  
   AllocationStamp:string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   BatchID:string,
      /**  This is the allocation id that processed this journal entry.  */  
   AllocID:string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was processed under.  */  
   RunNbr:number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   AllocRunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
   StatAmount:number,
   BitFlag:number,
   AHGLJrnDtlSimAlcHedTier:number,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  GL Account or GL Account mask  */  
   AllocGLAcct:string,
      /**  Allocation Segment Value 1  */  
   AllocSegValue1:string,
      /**  Allocation Segment Value 2  */  
   AllocSegValue2:string,
      /**  Allocation Segment Value 3  */  
   AllocSegValue3:string,
      /**  Allocation Segment Value 4  */  
   AllocSegValue4:string,
      /**  Allocation Segment Value 5  */  
   AllocSegValue5:string,
      /**  Allocation Segment Value 6  */  
   AllocSegValue6:string,
      /**  Allocation Segment Value 7  */  
   AllocSegValue7:string,
      /**  Allocation Segment Value 8  */  
   AllocSegValue8:string,
      /**  Allocation Segment Value 9  */  
   AllocSegValue9:string,
      /**  Allocation Segment Value 10  */  
   AllocSegValue10:string,
      /**  Allocation Segment Value 11  */  
   AllocSegValue11:string,
      /**  Allocation Segment Value 12  */  
   AllocSegValue12:string,
      /**  Allocation Segment Value 13  */  
   AllocSegValue13:string,
      /**  Allocation Segment Value 14  */  
   AllocSegValue14:string,
      /**  Allocation Segment Value 15  */  
   AllocSegValue15:string,
      /**  Allocation Segment Value 16  */  
   AllocSegValue16:string,
      /**  Allocation Segment Value 17  */  
   AllocSegValue17:string,
      /**  Allocation Segment Value 18  */  
   AllocSegValue18:string,
      /**  Allocation Segment Value 19  */  
   AllocSegValue19:string,
      /**  Allocation Segment Value 20  */  
   AllocSegValue20:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   AllocGLAcctGLShortAcct:string,
   AllocGLAcctAccountDesc:string,
   AllocGLAcctGLAcctDisp:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistActCatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique identifier of this category of accounts.  */  
   CategoryID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Yes indicates this record contains information about the amount written off against the source account.  NO indicates this record contains information about the amount allocated.  */  
   WriteOff:boolean,
      /**  Initial balance of the write off account.  Only updated when WriteOff = yes.  */  
   SourceInitBalance:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Source GL Account or Balance Account.  */  
   SourceAccount:string,
      /**  Account the source amount was allocated to.  */  
   TargetAccount:string,
      /**  REsolved GL Account.  This is the same as the target account if the target account does not have any mask characters.  */  
   ResolvedAccount:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  */  
   AllocUnits:number,
      /**  Postive, fractional value indicating how much of an allocation is applied to this target.  */  
   RatioValue:number,
      /**  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  */  
   RatioFormula:string,
      /**  Resolved Formula based upon the Ratio Formula.  Only valid if the allocation option = 2.  */  
   ResolvedFormula:string,
      /**  Yes indicates this entry is a reversing entry.  No indicates it is not a reversing entry.  */  
   ReversingEntry:boolean,
      /**  Target Segment Value 1  */  
   TgtSegVal1:string,
      /**  Target Segment Value 2  */  
   TgtSegVal2:string,
      /**  Target Segment Value 3  */  
   TgtSegVal3:string,
      /**  Target Segment Value 4  */  
   TgtSegVal4:string,
      /**  Target Segment Value 5  */  
   TgtSegVal5:string,
      /**  Target Segment Value 6  */  
   TgtSegVal6:string,
      /**  Target Segment Value 7  */  
   TgtSegVal7:string,
      /**  Target Segment Value 8  */  
   TgtSegVal8:string,
      /**  Target Segment Value 9  */  
   TgtSegVal9:string,
      /**  Target Segment Value 10  */  
   TgtSegVal10:string,
      /**  Target Segment Value 11  */  
   TgtSegVal11:string,
      /**  Target Segment Value 12  */  
   TgtSegVal12:string,
      /**  Target Segment Value 13  */  
   TgtSegVal13:string,
      /**  Target Segment Value 14  */  
   TgtSegVal14:string,
      /**  Target Segment Value 15  */  
   TgtSegVal15:string,
      /**  Target Segment Value 16  */  
   TgtSegVal16:string,
      /**  Target Segment Value 17  */  
   TgtSegVal17:string,
      /**  Target Segment Value 18  */  
   TgtSegVal18:string,
      /**  Target Segment Value 19  */  
   TgtSegVal19:string,
      /**  Target Segment Value 20  */  
   TgtSegVal20:string,
      /**  Source Segment Value 1  */  
   SrcSegVal1:string,
      /**  Source Segment Value 2  */  
   SrcSegVal2:string,
      /**  Source Segment Value 3  */  
   SrcSegVal3:string,
      /**  Source Segment Value 4  */  
   SrcSegVal4:string,
      /**  Source Segment Value 5  */  
   SrcSegVal5:string,
      /**  Source Segment Value 6  */  
   SrcSegVal6:string,
      /**  Source Segment Value 7  */  
   SrcSegVal7:string,
      /**  Source Segment Value 8  */  
   SrcSegVal8:string,
      /**  Source Segment Value 9  */  
   SrcSegVal9:string,
      /**  Source Segment Value 10  */  
   SrcSegVal10:string,
      /**  Source Segment Value 11  */  
   SrcSegVal11:string,
      /**  Source Segment Value 12  */  
   SrcSegVal12:string,
      /**  Source Segment Value 13  */  
   SrcSegVal13:string,
      /**  Source Segment Value 14  */  
   SrcSegVal14:string,
      /**  Source Segment Value 15  */  
   SrcSegVal15:string,
      /**  Source Segment Value 16  */  
   SrcSegVal16:string,
      /**  Source Segment Value 17  */  
   SrcSegVal17:string,
      /**  Source Segment Value 18  */  
   SrcSegVal18:string,
      /**  Source Segment Value 19  */  
   SrcSegVal19:string,
      /**  Source Segment Value 20  */  
   SrcSegVal20:string,
      /**  Resolved Segment Value 1  */  
   ResSegVal1:string,
      /**  Resolved Segment Value 2  */  
   ResSegVal2:string,
      /**  Resolved Segment Value 3  */  
   ResSegVal3:string,
      /**  Resolved Segment Value 4  */  
   ResSegVal4:string,
      /**  Resolved Segment Value 5  */  
   ResSegVal5:string,
      /**  Resolved Segment Value 6  */  
   ResSegVal6:string,
      /**  Resolved Segment Value 7  */  
   ResSegVal7:string,
      /**  Resolved Segment Value 8  */  
   ResSegVal8:string,
      /**  Resolved Segment Value 9  */  
   ResSegVal9:string,
      /**  Resolved Segment Value 10  */  
   ResSegVal10:string,
      /**  Resolved Segment Value 11  */  
   ResSegVal11:string,
      /**  Resolved Segment Value 12  */  
   ResSegVal12:string,
      /**  Resolved Segment Value 13  */  
   ResSegVal13:string,
      /**  Resolved Segment Value 14  */  
   ResSegVal14:string,
      /**  Resolved Segment Value 15  */  
   ResSegVal15:string,
      /**  Resolved Segment Value 16  */  
   ResSegVal16:string,
      /**  Resolved Segment Value 17  */  
   ResSegVal17:string,
      /**  Resolved Segment Value 18  */  
   ResSegVal18:string,
      /**  Resolved Segment Value 19  */  
   ResSegVal19:string,
      /**  Resolved Segment Value 20  */  
   ResSegVal20:string,
      /**  The reversed fiscal year.  This is updated by reverse allocation run logic.  */  
   ReverseFY:number,
      /**   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated by reverse allocation run logic.  */  
   ReverseFYS:string,
      /**   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated by reverse allocation run logic.  */  
   ReverseJournalNum:number,
      /**   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a
.specific Company/FiscalYear/JournalNum combination and adding 1.This is updated by reverse allocation run logic  */  
   ReverseJournalLine:number,
      /**  Source amount applied to the formula/percentage during an allocation.  */  
   SrcDebitAmount:number,
      /**  Source amount applied to the formula/percentage during an allocation.  */  
   SrcCreditAmount:number,
      /**  The reversed entry fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   RevEntryFY:number,
      /**   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   RevEntryFYS:string,
      /**   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   RevEntryJrnlNum:number,
      /**   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  */  
   RevEntryJrnlLine:number,
      /**  The reversed entry reversing fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and the reversing journal entry is reversed.  */  
   RevReverseFY:number,
      /**   The reversed reversing entry fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  */  
   RevReverseFYS:string,
      /**   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  */  
   RevReverseJrnlNum:number,
      /**   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  */  
   RevReverseJrnlLine:number,
      /**  Cycle unique ID.  This is not intended for external use.  */  
   CycleUID:number,
      /**  Cycle number.  */  
   CycleNumber:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   GLAccount:string,
   CreditAmount:number,
   DebitAmount:number,
   JEDate:string,
   BitFlag:number,
   AlcHistDtlAlcHedTier:number,
   AlcHistDtlJrnlCdJrnlDescription:string,
   ResolvedGLAcctDispGLShortAcct:string,
   ResolvedGLAcctDispGLAcctDisp:string,
   ResolvedGLAcctDispAccountDesc:string,
   SourceAccountAccountDesc:string,
   SourceAccountGLShortAcct:string,
   SourceAccountGLAcctDisp:string,
   TargetAccountAccountDesc:string,
   TargetAccountGLShortAcct:string,
   TargetAccountGLAcctDisp:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistJrnCdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   JournalCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   JrnlCodeJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Date the batch was run.  */  
   RunDate:string,
      /**  Time the allocaiton batch run started.  */  
   RunTime:number,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  User ID  */  
   DcdUserID:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Indicates if this is simulation history record or General Ledger history record.  */  
   Simulation:boolean,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Apply Date for journal transactions.  */  
   ApplyDate:string,
      /**  Date used for reversing entries.  */  
   ApplyDateRev:string,
      /**  Starting date for record selection.  Defaults to the fiscal period start date.  */  
   StartDate:string,
      /**  Ending date for record seletion.  Defaults to fiscal period end date.  */  
   EndDate:string,
      /**  Date when the allocation batch is due to be run.  */  
   SchedDate:string,
      /**  Batch Description  */  
   BatchDesc:string,
      /**  Allocation tier.  */  
   Tier:number,
      /**  Internal next number used to keep the schedule records unique.  */  
   SchedNum:number,
      /**  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  */  
   Reverse:boolean,
      /**  Indicates if the allocation run started at the beginning of the current fiscal year.  */  
   YTDAlloc:boolean,
      /**  Indicates if the allocation run has been reversed.  */  
   AllocReversed:boolean,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   PriorTgtStamp:string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   TgtStamp:string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   SrcAllocStamp:string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   IgnoreStamp:boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   UseAllStamps:boolean,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   PercentToAlloc:number,
      /**  Indicates if the allocation units are used.  */  
   UseAllocUnits:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RunTypeDesc:string,
      /**  Calendar description.  */  
   AlcHistFiscalCalDescription:string,
      /**  Indicates the base currency for the book  */  
   AlcHistGLBookCurrencyCode:string,
      /**  Descripiton of Book  */  
   AlcHistGLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistListTableset{
   AlcHistList:Erp_Tablesets_AlcHistListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AlcHistNFSrcRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. The value of ParamNbr identifies the parameter number the record is defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  LookupTblMapUID_obsolete  */  
   LookupTblMapUID_obsolete:number,
      /**  TgtSeqNbr_obsolete  */  
   TgtSeqNbr_obsolete:number,
      /**  LinkUID_obsolete  */  
   LinkUID_obsolete:number,
      /**  Source field name.  */  
   SrcFieldName:string,
      /**   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   ParamOpt:number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   ParamSegmentNbr:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   EntryType:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SrcSeqNbr  */  
   SrcSeqNbr:number,
      /**  SrcCodeID  */  
   SrcCodeID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistParamsBAQRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Intended for internal use only to keep the records unique.  */  
   ParamNbr:number,
      /**  BAQ ID, the unique identifier for this Query table within the company  */  
   BAQExportID:string,
      /**  Intended for internal use only to keep the records unique.  */  
   BAQParamValNbr:number,
   ParameterName:string,
      /**  Specific baq parameter value.  */  
   BAQParamCode:string,
      /**   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  */  
   ParamOpt:number,
      /**  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  */  
   ParamSegmentNbr:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies if the parameter is an actual value or an option.  */  
   EntryType:number,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistParamsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  The name assigned to a parameter.  This name must be unique.  */  
   ParamName:string,
      /**  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances and 3 = BAQ.  */  
   ParamType:number,
      /**  Text that describes the parameter.  */  
   ParamDesc:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Account balance account.  Only valid when the formula type = 1.  */  
   AcctBalAcct:string,
      /**  Account Segment Value 1  */  
   AcctBalSegVal1:string,
      /**  Account Segment Value 2  */  
   AcctBalSegVal2:string,
      /**  Account Segment Value 3  */  
   AcctBalSegVal3:string,
      /**  Account Segment Value 4  */  
   AcctBalSegVal4:string,
      /**  Account Segment Value 5  */  
   AcctBalSegVal5:string,
      /**  Account Segment Value 6  */  
   AcctBalSegVal6:string,
      /**  Account Segment Value 7  */  
   AcctBalSegVal7:string,
      /**  Account Segment Value 8  */  
   AcctBalSegVal8:string,
      /**  Account Segment Value 9  */  
   AcctBalSegVal9:string,
      /**  Account Segment Value 10  */  
   AcctBalSegVal10:string,
      /**  Account Segment Value 11  */  
   AcctBalSegVal11:string,
      /**  Account Segment Value 12  */  
   AcctBalSegVal12:string,
      /**  Account Segment Value 13  */  
   AcctBalSegVal13:string,
      /**  Account Segment Value 14  */  
   AcctBalSegVal14:string,
      /**  Account Segment Value 15  */  
   AcctBalSegVal15:string,
      /**  Account Segment Value 16  */  
   AcctBalSegVal16:string,
      /**  Account Segment Value 17  */  
   AcctBalSegVal17:string,
      /**  Account Segment Value 18  */  
   AcctBalSegVal18:string,
      /**  Account Segment Value 19  */  
   AcctBalSegVal19:string,
      /**  Account Segment Value 20  */  
   AcctBalSegVal20:string,
      /**  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  */  
   UseTgtAcct:boolean,
      /**  BAQ  ID, the unique identifier for the query table within the company  */  
   BAQExportID:string,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  */  
   AcctParamValSrc:number,
      /**  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  */  
   SumParamValSrc:number,
      /**  Indicates if the allocation run was reversed.  */  
   Reversed:boolean,
      /**  Date used to reverse the allocation run.  */  
   ReversedDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NFSrcMapUID  */  
   NFSrcMapUID:number,
      /**  NFTgtSeqNbr  */  
   NFTgtSeqNbr:number,
      /**  YTDBalance  */  
   YTDBalance:boolean,
   BitFlag:number,
   AcctBalAcctGLAcctDispAccountDesc:string,
   AcctBalAcctGLAcctDispGLShortAcct:string,
   AcctBalAcctGLAcctDispGLAcctDisp:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistRangeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Minimum vale for range selection.  */  
   MinValue:string,
      /**  Maximum value for range selection.  */  
   MaxValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   COASegmentSegmentName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistResParamsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  Intended for internal use only to keep the records unique.  */  
   ParamNbr:number,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Actual calculated value.  */  
   ActualValue:number,
      /**  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  */  
   ResBalAcct:string,
      /**  Resolved  Segment Value 1  */  
   ResBalSegVal1:string,
      /**  Resolved  Segment Value 2  */  
   ResBalSegVal2:string,
      /**  Resolved  Segment Value 3  */  
   ResBalSegVal3:string,
      /**  Resolved Segment Value 4  */  
   ResBalSegVal4:string,
      /**  Resolved  Segment Value 5  */  
   ResBalSegVal5:string,
      /**  Resolved  Segment Value 6  */  
   ResBalSegVal6:string,
      /**  Resolved Segment Value 7  */  
   ResBalSegVal7:string,
      /**  Resolved  Segment Value 8  */  
   ResBalSegVal8:string,
      /**  Resolved  Segment Value 9  */  
   ResBalSegVal9:string,
      /**  Resolved Segment Value 10  */  
   ResBalSegVal10:string,
      /**  Resolved Segment Value 11  */  
   ResBalSegVal11:string,
      /**  Resolved  Segment Value 12  */  
   ResBalSegVal12:string,
      /**  Resolved  Segment Value 13  */  
   ResBalSegVal13:string,
      /**  Resolved  Segment Value 14  */  
   ResBalSegVal14:string,
      /**  Resolved Segment Value 15  */  
   ResBalSegVal15:string,
      /**  Resolved  Segment Value 16  */  
   ResBalSegVal16:string,
      /**  Resolved  Segment Value 17  */  
   ResBalSegVal17:string,
      /**  Resolved  Segment Value 18  */  
   ResBalSegVal18:string,
      /**  Resolved Segment Value 19  */  
   ResBalSegVal19:string,
      /**  Resolved  Segment Value 20  */  
   ResBalSegVal20:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Cycle unique ID.  This is not intended for external use.  */  
   CycleUID:number,
      /**  Cycle number.  */  
   CycleNumber:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  YTDBalance  */  
   YTDBalance:boolean,
   AcctBalAcct:string,
   UseTgtAcct:boolean,
   BAQExportID:string,
   AcctParamValSrc:number,
   SumParamValSrc:number,
   TgtGLAcct:string,
   BitFlag:number,
   AlcHistParamsParamType:number,
   AlcHistParamsAcctParamValSrc:number,
   AlcHistParamsUseTgtAcct:boolean,
   AlcHistParamsParamName:string,
   AlcHistParamsSumParamValSrc:number,
   AlcHistParamsBAQExportID:string,
   AlcHistParamsAcctBalAcct:string,
   AlcHistParamsParamDesc:string,
   ResAcctDispGLShortAcct:string,
   ResAcctDispGLAcctDisp:string,
   ResAcctDispAccountDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistResParamsSimRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  Intended for internal use only to keep the records unique.  */  
   ParamNbr:number,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Actual calculated value.  */  
   ActualValue:number,
      /**  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  */  
   ResBalAcct:string,
      /**  Resolved  Segment Value 1  */  
   ResBalSegVal1:string,
      /**  Resolved  Segment Value 2  */  
   ResBalSegVal2:string,
      /**  Resolved  Segment Value 3  */  
   ResBalSegVal3:string,
      /**  Resolved Segment Value 4  */  
   ResBalSegVal4:string,
      /**  Resolved  Segment Value 5  */  
   ResBalSegVal5:string,
      /**  Resolved  Segment Value 6  */  
   ResBalSegVal6:string,
      /**  Resolved Segment Value 7  */  
   ResBalSegVal7:string,
      /**  Resolved  Segment Value 8  */  
   ResBalSegVal8:string,
      /**  Resolved  Segment Value 9  */  
   ResBalSegVal9:string,
      /**  Resolved Segment Value 10  */  
   ResBalSegVal10:string,
      /**  Resolved Segment Value 11  */  
   ResBalSegVal11:string,
      /**  Resolved  Segment Value 12  */  
   ResBalSegVal12:string,
      /**  Resolved  Segment Value 13  */  
   ResBalSegVal13:string,
      /**  Resolved  Segment Value 14  */  
   ResBalSegVal14:string,
      /**  Resolved Segment Value 15  */  
   ResBalSegVal15:string,
      /**  Resolved  Segment Value 16  */  
   ResBalSegVal16:string,
      /**  Resolved  Segment Value 17  */  
   ResBalSegVal17:string,
      /**  Resolved  Segment Value 18  */  
   ResBalSegVal18:string,
      /**  Resolved Segment Value 19  */  
   ResBalSegVal19:string,
      /**  Resolved  Segment Value 20  */  
   ResBalSegVal20:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Cycle unique ID.  This is not intended for external use.  */  
   CycleUID:number,
      /**  Cycle number.  */  
   CycleNumber:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  YTDBalance  */  
   YTDBalance:boolean,
   TgtGLAcct:string,
   BitFlag:number,
   AlcHistParamsSimSumParamValSrc:number,
   AlcHistParamsSimParamName:string,
   AlcHistParamsSimParamType:number,
   AlcHistParamsSimAcctBalAcct:string,
   AlcHistParamsSimParamDesc:string,
   AlcHistParamsSimUseTgtAcct:boolean,
   AlcHistParamsSimAcctParamValSrc:number,
   ResAcctDispSimGLAcctDisp:string,
   ResAcctDispSimGLShortAcct:string,
   ResAcctDispSimAccountDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Date the batch was run.  */  
   RunDate:string,
      /**  Time the allocaiton batch run started.  */  
   RunTime:number,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  User ID  */  
   DcdUserID:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Indicates if this is simulation history record or General Ledger history record.  */  
   Simulation:boolean,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  Apply Date for journal transactions.  */  
   ApplyDate:string,
      /**  Date used for reversing entries.  */  
   ApplyDateRev:string,
      /**  Starting date for record selection.  Defaults to the fiscal period start date.  */  
   StartDate:string,
      /**  Ending date for record seletion.  Defaults to fiscal period end date.  */  
   EndDate:string,
      /**  Date when the allocation batch is due to be run.  */  
   SchedDate:string,
      /**  Batch Description  */  
   BatchDesc:string,
      /**  Allocation tier.  */  
   Tier:number,
      /**  Internal next number used to keep the schedule records unique.  */  
   SchedNum:number,
      /**  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  */  
   Reverse:boolean,
      /**  Indicates if the allocation run started at the beginning of the current fiscal year.  */  
   YTDAlloc:boolean,
      /**  Indicates if the allocation run has been reversed.  */  
   AllocReversed:boolean,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   PriorTgtStamp:string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   TgtStamp:string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   SrcAllocStamp:string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   IgnoreStamp:boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   UseAllStamps:boolean,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   PercentToAlloc:number,
      /**  Indicates if the allocation units are used.  */  
   UseAllocUnits:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  StatBalAsAllocUnits  */  
   StatBalAsAllocUnits:boolean,
   RunTypeDesc:string,
   BitFlag:number,
   AlcHistFiscalCalDescription:string,
   AlcHistGLBookCurrencyCode:string,
   AlcHistGLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistoryFilterRow{
   BookID:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   StartPeriod:number,
   EndPeriod:number,
   RunType:number,
   RunTypeDesc:string,
   BookDesc:string,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHistoryFilterTableset{
   AlcHistoryFilter:Erp_Tablesets_AlcHistoryFilterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AlcHistoryTableset{
   AlcHist:Erp_Tablesets_AlcHistRow[],
   AHGLJrnDtl:Erp_Tablesets_AHGLJrnDtlRow[],
   AlcHistResParams:Erp_Tablesets_AlcHistResParamsRow[],
   AHGLJrnDtlSim:Erp_Tablesets_AHGLJrnDtlSimRow[],
   AlcHistResParamsSim:Erp_Tablesets_AlcHistResParamsSimRow[],
   AlcHistAcct:Erp_Tablesets_AlcHistAcctRow[],
   AlcHistActCat:Erp_Tablesets_AlcHistActCatRow[],
   AlcHistDtl:Erp_Tablesets_AlcHistDtlRow[],
   AlcHistJrnCd:Erp_Tablesets_AlcHistJrnCdRow[],
   AlcHistParams:Erp_Tablesets_AlcHistParamsRow[],
   AlcHistParamsBAQ:Erp_Tablesets_AlcHistParamsBAQRow[],
   AlcHistNFSrc:Erp_Tablesets_AlcHistNFSrcRow[],
   PAlcHistAcct:Erp_Tablesets_PAlcHistAcctRow[],
   PAlcHistActCat:Erp_Tablesets_PAlcHistActCatRow[],
   PAlcHistJrnCd:Erp_Tablesets_PAlcHistJrnCdRow[],
   PAlcHistRange:Erp_Tablesets_PAlcHistRangeRow[],
   AlcHistRange:Erp_Tablesets_AlcHistRangeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PAlcHistAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  GL Account or GL Account mask  */  
   AllocGLAcct:string,
      /**  Allocation Segment Value 1  */  
   AllocSegValue1:string,
      /**  Allocation Segment Value 2  */  
   AllocSegValue2:string,
      /**  Allocation Segment Value 3  */  
   AllocSegValue3:string,
      /**  Allocation Segment Value 4  */  
   AllocSegValue4:string,
      /**  Allocation Segment Value 5  */  
   AllocSegValue5:string,
      /**  Allocation Segment Value 6  */  
   AllocSegValue6:string,
      /**  Allocation Segment Value 7  */  
   AllocSegValue7:string,
      /**  Allocation Segment Value 8  */  
   AllocSegValue8:string,
      /**  Allocation Segment Value 9  */  
   AllocSegValue9:string,
      /**  Allocation Segment Value 10  */  
   AllocSegValue10:string,
      /**  Allocation Segment Value 11  */  
   AllocSegValue11:string,
      /**  Allocation Segment Value 12  */  
   AllocSegValue12:string,
      /**  Allocation Segment Value 13  */  
   AllocSegValue13:string,
      /**  Allocation Segment Value 14  */  
   AllocSegValue14:string,
      /**  Allocation Segment Value 15  */  
   AllocSegValue15:string,
      /**  Allocation Segment Value 16  */  
   AllocSegValue16:string,
      /**  Allocation Segment Value 17  */  
   AllocSegValue17:string,
      /**  Allocation Segment Value 18  */  
   AllocSegValue18:string,
      /**  Allocation Segment Value 19  */  
   AllocSegValue19:string,
      /**  Allocation Segment Value 20  */  
   AllocSegValue20:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PAllocGLAccountGLAcctDisp:string,
   PAllocGLAccountGLShortAcct:string,
   PAllocGLAccountAccountDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PAlcHistActCatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique identifier of this category of accounts.  */  
   CategoryID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PAlcHistJrnCdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  */  
   JournalCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PHistJrnlCodeJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PAlcHistRangeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The batch code is the identifier of a group of allocation codes scheduled to run together.  */  
   BatchID:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  */  
   ParamNbr:number,
      /**  System generated next number used to keep data unique for allocation batch runs.  */  
   RunNbr:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  1 = General Ledger, 2 = Simulation  */  
   RunType:number,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Minimum vale for range selection.  */  
   MinValue:string,
      /**  Maximum value for range selection.  */  
   MaxValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PCOASegmentSegmentName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAlcHistoryTableset{
   AlcHist:Erp_Tablesets_AlcHistRow[],
   AHGLJrnDtl:Erp_Tablesets_AHGLJrnDtlRow[],
   AlcHistResParams:Erp_Tablesets_AlcHistResParamsRow[],
   AHGLJrnDtlSim:Erp_Tablesets_AHGLJrnDtlSimRow[],
   AlcHistResParamsSim:Erp_Tablesets_AlcHistResParamsSimRow[],
   AlcHistAcct:Erp_Tablesets_AlcHistAcctRow[],
   AlcHistActCat:Erp_Tablesets_AlcHistActCatRow[],
   AlcHistDtl:Erp_Tablesets_AlcHistDtlRow[],
   AlcHistJrnCd:Erp_Tablesets_AlcHistJrnCdRow[],
   AlcHistParams:Erp_Tablesets_AlcHistParamsRow[],
   AlcHistParamsBAQ:Erp_Tablesets_AlcHistParamsBAQRow[],
   AlcHistNFSrc:Erp_Tablesets_AlcHistNFSrcRow[],
   PAlcHistAcct:Erp_Tablesets_PAlcHistAcctRow[],
   PAlcHistActCat:Erp_Tablesets_PAlcHistActCatRow[],
   PAlcHistJrnCd:Erp_Tablesets_PAlcHistJrnCdRow[],
   PAlcHistRange:Erp_Tablesets_PAlcHistRangeRow[],
   AlcHistRange:Erp_Tablesets_AlcHistRangeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param batchID
      @param runNbr
   */  
export interface GetByBatchIDRunNbr_input{
   batchID:string,
   runNbr:number,
}

export interface GetByBatchIDRunNbr_output{
   returnObj:Erp_Tablesets_AlcHistoryTableset[],
}

   /** Required : 
      @param batchID
      @param runNbr
      @param allocID
   */  
export interface GetByID_input{
   batchID:string,
   runNbr:number,
   allocID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AlcHistoryTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AlcHistoryTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AlcHistoryTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListByBatchID_input{
      /**  Whereclause.  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListByBatchID_output{
   returnObj:Erp_Tablesets_AlcHistListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
   returnObj:Erp_Tablesets_AlcHistListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param allocTgtNbr
      @param allocTgtSeq
   */  
export interface GetNewAHGLJrnDtlSim_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   allocTgtNbr:number,
   allocTgtSeq:number,
}

export interface GetNewAHGLJrnDtlSim_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param allocTgtNbr
      @param allocTgtSeq
   */  
export interface GetNewAHGLJrnDtl_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   allocTgtNbr:number,
   allocTgtSeq:number,
}

export interface GetNewAHGLJrnDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcHistAcct_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcHistAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcHistActCat_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcHistActCat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param allocTgtNbr
   */  
export interface GetNewAlcHistDtl_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   allocTgtNbr:number,
}

export interface GetNewAlcHistDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcHistJrnCd_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcHistJrnCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcHistNFSrc_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcHistNFSrc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
      @param baQExportID
   */  
export interface GetNewAlcHistParamsBAQ_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
   baQExportID:string,
}

export interface GetNewAlcHistParamsBAQ_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
   */  
export interface GetNewAlcHistParams_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
}

export interface GetNewAlcHistParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewAlcHistRange_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewAlcHistRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param allocTgtNbr
      @param allocTgtSeq
   */  
export interface GetNewAlcHistResParamsSim_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   allocTgtNbr:number,
   allocTgtSeq:number,
}

export interface GetNewAlcHistResParamsSim_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param allocTgtNbr
      @param allocTgtSeq
   */  
export interface GetNewAlcHistResParams_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   allocTgtNbr:number,
   allocTgtSeq:number,
}

export interface GetNewAlcHistResParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
   */  
export interface GetNewAlcHist_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
}

export interface GetNewAlcHist_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

export interface GetNewAlcHistoryFilter_output{
   returnObj:Erp_Tablesets_AlcHistoryFilterTableset[],
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewPAlcHistAcct_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewPAlcHistAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewPAlcHistActCat_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewPAlcHistActCat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewPAlcHistJrnCd_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewPAlcHistJrnCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param ds
      @param batchID
      @param runNbr
      @param allocID
      @param paramNbr
   */  
export interface GetNewPAlcHistRange_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
   batchID:string,
   runNbr:number,
   allocID:string,
   paramNbr:number,
}

export interface GetNewPAlcHistRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

   /** Required : 
      @param whereClauseAlcHist
      @param whereClauseAHGLJrnDtl
      @param whereClauseAlcHistResParams
      @param whereClauseAHGLJrnDtlSim
      @param whereClauseAlcHistResParamsSim
      @param whereClauseAlcHistAcct
      @param whereClauseAlcHistActCat
      @param whereClauseAlcHistDtl
      @param whereClauseAlcHistJrnCd
      @param whereClauseAlcHistParams
      @param whereClauseAlcHistParamsBAQ
      @param whereClauseAlcHistNFSrc
      @param whereClausePAlcHistAcct
      @param whereClausePAlcHistActCat
      @param whereClausePAlcHistJrnCd
      @param whereClausePAlcHistRange
      @param whereClauseAlcHistRange
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAlcHist:string,
   whereClauseAHGLJrnDtl:string,
   whereClauseAlcHistResParams:string,
   whereClauseAHGLJrnDtlSim:string,
   whereClauseAlcHistResParamsSim:string,
   whereClauseAlcHistAcct:string,
   whereClauseAlcHistActCat:string,
   whereClauseAlcHistDtl:string,
   whereClauseAlcHistJrnCd:string,
   whereClauseAlcHistParams:string,
   whereClauseAlcHistParamsBAQ:string,
   whereClauseAlcHistNFSrc:string,
   whereClausePAlcHistAcct:string,
   whereClausePAlcHistActCat:string,
   whereClausePAlcHistJrnCd:string,
   whereClausePAlcHistRange:string,
   whereClauseAlcHistRange:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AlcHistoryTableset[],
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
      @param cInBookID
   */  
export interface OnChangeBookID_input{
      /**  Proposed BookID  */  
   cInBookID:string,
}

export interface OnChangeBookID_output{
parameters : {
      /**  output parameters  */  
   fiscalCalendarID:string,
   iOutFiscalYear:number,
   cOutFiscalYearSuffix:string,
   iOutStartPeriod:number,
   iOutEndPeriod:number,
}
}

   /** Required : 
      @param bookID
      @param fiscalYear
      @param fiscalYearSuffix
      @param selectedStartPeriod
      @param selectedEndPeriod
   */  
export interface OnChangeFiscalYearOrSuffix_input{
   bookID:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
   selectedStartPeriod:number,
   selectedEndPeriod:number,
}

export interface OnChangeFiscalYearOrSuffix_output{
parameters : {
      /**  output parameters  */  
   startPeriod:number,
   endPeriod:number,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAlcHistoryTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAlcHistoryTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AlcHistoryTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHistoryTableset[],
}
}

