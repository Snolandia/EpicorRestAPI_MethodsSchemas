import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PcLookupTblSvc
// Description: PcLookupTbl Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/$metadata", {
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
   Description: Get PcLookupTbls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupTbls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblHedRow
   */  
export function get_PcLookupTbls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupTbls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcLookupTbls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls", {
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
   Summary: Calls GetByID to retrieve the PcLookupTbl item
   Description: Calls GetByID to retrieve the PcLookupTbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupTbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
   */  
export function get_PcLookupTbls_Company_LookupTblID(Company:string, LookupTblID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcLookupTblHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls(" + Company + "," + LookupTblID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcLookupTblHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcLookupTbl for the service
   Description: Calls UpdateExt to update PcLookupTbl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupTbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcLookupTbls_Company_LookupTblID(Company:string, LookupTblID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls(" + Company + "," + LookupTblID + ")", {
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
   Summary: Call UpdateExt to delete PcLookupTbl item
   Description: Call UpdateExt to delete PcLookupTbl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupTbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcLookupTbls_Company_LookupTblID(Company:string, LookupTblID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTbls(" + Company + "," + LookupTblID + ")", {
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
   Description: Get PcLookupTblHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupTblHedAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblHedAttchRow
   */  
export function get_PcLookupTblHedAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupTblHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcLookupTblHedAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches", {
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
   Summary: Calls GetByID to retrieve the PcLookupTblHedAttch item
   Description: Calls GetByID to retrieve the PcLookupTblHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupTblHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
   */  
export function get_PcLookupTblHedAttches_Company_LookupTblID_DrawingSeq(Company:string, LookupTblID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcLookupTblHedAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches(" + Company + "," + LookupTblID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcLookupTblHedAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcLookupTblHedAttch for the service
   Description: Calls UpdateExt to update PcLookupTblHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupTblHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupTblHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcLookupTblHedAttches_Company_LookupTblID_DrawingSeq(Company:string, LookupTblID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches(" + Company + "," + LookupTblID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PcLookupTblHedAttch item
   Description: Call UpdateExt to delete PcLookupTblHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupTblHedAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcLookupTblHedAttches_Company_LookupTblID_DrawingSeq(Company:string, LookupTblID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblHedAttches(" + Company + "," + LookupTblID + "," + DrawingSeq + ")", {
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
   Description: Get PcLookupColSetHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupColSetHeds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupColSetHedRow
   */  
export function get_PcLookupColSetHeds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupColSetHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcLookupColSetHeds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds", {
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
   Summary: Calls GetByID to retrieve the PcLookupColSetHed item
   Description: Calls GetByID to retrieve the PcLookupColSetHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupColSetHed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
   */  
export function get_PcLookupColSetHeds_Company_LookupTblID_ColSetID(Company:string, LookupTblID:string, ColSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcLookupColSetHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds(" + Company + "," + LookupTblID + "," + ColSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcLookupColSetHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcLookupColSetHed for the service
   Description: Calls UpdateExt to update PcLookupColSetHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupColSetHed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcLookupColSetHeds_Company_LookupTblID_ColSetID(Company:string, LookupTblID:string, ColSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds(" + Company + "," + LookupTblID + "," + ColSetID + ")", {
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
   Summary: Call UpdateExt to delete PcLookupColSetHed item
   Description: Call UpdateExt to delete PcLookupColSetHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupColSetHed
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcLookupColSetHeds_Company_LookupTblID_ColSetID(Company:string, LookupTblID:string, ColSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetHeds(" + Company + "," + LookupTblID + "," + ColSetID + ")", {
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
   Description: Get PcLookupColSetDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupColSetDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupColSetDtlRow
   */  
export function get_PcLookupColSetDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupColSetDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcLookupColSetDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls", {
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
   Summary: Calls GetByID to retrieve the PcLookupColSetDtl item
   Description: Calls GetByID to retrieve the PcLookupColSetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupColSetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColName Desc: ColName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
   */  
export function get_PcLookupColSetDtls_Company_LookupTblID_ColSetID_ColName(Company:string, LookupTblID:string, ColSetID:string, ColName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcLookupColSetDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls(" + Company + "," + LookupTblID + "," + ColSetID + "," + ColName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcLookupColSetDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcLookupColSetDtl for the service
   Description: Calls UpdateExt to update PcLookupColSetDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupColSetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColName Desc: ColName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupColSetDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcLookupColSetDtls_Company_LookupTblID_ColSetID_ColName(Company:string, LookupTblID:string, ColSetID:string, ColName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls(" + Company + "," + LookupTblID + "," + ColSetID + "," + ColName + ")", {
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
   Summary: Call UpdateExt to delete PcLookupColSetDtl item
   Description: Call UpdateExt to delete PcLookupColSetDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupColSetDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColName Desc: ColName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcLookupColSetDtls_Company_LookupTblID_ColSetID_ColName(Company:string, LookupTblID:string, ColSetID:string, ColName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupColSetDtls(" + Company + "," + LookupTblID + "," + ColSetID + "," + ColName + ")", {
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
   Description: Get PcLookupTblValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcLookupTblValues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblValuesRow
   */  
export function get_PcLookupTblValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcLookupTblValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcLookupTblValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues", {
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
   Summary: Calls GetByID to retrieve the PcLookupTblValue item
   Description: Calls GetByID to retrieve the PcLookupTblValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcLookupTblValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param RowNum Desc: RowNum   Required: True
      @param ColName Desc: ColName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
   */  
export function get_PcLookupTblValues_Company_LookupTblID_RowNum_ColName(Company:string, LookupTblID:string, RowNum:string, ColName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcLookupTblValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues(" + Company + "," + LookupTblID + "," + RowNum + "," + ColName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcLookupTblValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcLookupTblValue for the service
   Description: Calls UpdateExt to update PcLookupTblValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcLookupTblValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param RowNum Desc: RowNum   Required: True
      @param ColName Desc: ColName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcLookupTblValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcLookupTblValues_Company_LookupTblID_RowNum_ColName(Company:string, LookupTblID:string, RowNum:string, ColName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues(" + Company + "," + LookupTblID + "," + RowNum + "," + ColName + ")", {
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
   Summary: Call UpdateExt to delete PcLookupTblValue item
   Description: Call UpdateExt to delete PcLookupTblValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcLookupTblValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LookupTblID Desc: LookupTblID   Required: True   Allow empty value : True
      @param RowNum Desc: RowNum   Required: True
      @param ColName Desc: ColName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcLookupTblValues_Company_LookupTblID_RowNum_ColName(Company:string, LookupTblID:string, RowNum:string, ColName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/PcLookupTblValues(" + Company + "," + LookupTblID + "," + RowNum + "," + ColName + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcLookupTblListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePcLookupTblHed:string, whereClausePcLookupTblHedAttch:string, whereClausePcLookupColSetHed:string, whereClausePcLookupColSetDtl:string, whereClausePcLookupTblValues:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcLookupTblHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcLookupTblHed=" + whereClausePcLookupTblHed
   }
   if(typeof whereClausePcLookupTblHedAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcLookupTblHedAttch=" + whereClausePcLookupTblHedAttch
   }
   if(typeof whereClausePcLookupColSetHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcLookupColSetHed=" + whereClausePcLookupColSetHed
   }
   if(typeof whereClausePcLookupColSetDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcLookupColSetDtl=" + whereClausePcLookupColSetDtl
   }
   if(typeof whereClausePcLookupTblValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcLookupTblValues=" + whereClausePcLookupTblValues
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(lookupTblID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof lookupTblID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lookupTblID=" + lookupTblID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetList" + params, {
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
   Summary: Invoke method GetDisplayColumns
   Description: Generate Columns that will be displayed in the grid
   OperationID: GetDisplayColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDisplayColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisplayColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDisplayColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetDisplayColumns", {
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
   Summary: Invoke method GetFormatOptions
   Description: Get the valid options that are used for populating format options.
   OperationID: GetFormatOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFormatOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormatOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFormatOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetFormatOptions", {
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
   Summary: Invoke method ImportPcLookupTblFromCSV
   Description: Create a new PCLookupImportExportTableset from the imported CSV file and then call the ImportPcLookupTbl to insert it into the database.
   OperationID: ImportPcLookupTblFromCSV
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTblFromCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTblFromCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportPcLookupTblFromCSV(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ImportPcLookupTblFromCSV", {
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
   Summary: Invoke method ImportPcLookupTbl
   Description: Inserts values into database from the imported file.
   OperationID: ImportPcLookupTbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportPcLookupTbl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ImportPcLookupTbl", {
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
   Summary: Invoke method GetExportPcLookupTables
   Description: Gets the PcLookupTbl records set to export
   OperationID: GetExportPcLookupTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExportPcLookupTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExportPcLookupTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExportPcLookupTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetExportPcLookupTables", {
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
   Summary: Invoke method GetDataTable
   OperationID: GetDataTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetDataTable", {
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
   Summary: Invoke method CopyColSet
   Description: Copy column set from source to desctination.
   OperationID: CopyColSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyColSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyColSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyColSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/CopyColSet", {
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
   Summary: Invoke method UpdateLookupTblValue
   Description: Update lookup table value
   OperationID: UpdateLookupTblValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLookupTblValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLookupTblValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLookupTblValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/UpdateLookupTblValue", {
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
   Summary: Invoke method DeleteLookupTblValue
   Description: Delete lookup table row
   OperationID: DeleteLookupTblValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLookupTblValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLookupTblValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLookupTblValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/DeleteLookupTblValue", {
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
   Summary: Invoke method GetNewPcLookupTblDisplay
   Description: Creates new Lookup table row
   OperationID: GetNewPcLookupTblDisplay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblDisplay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblDisplay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcLookupTblDisplay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetNewPcLookupTblDisplay", {
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
   Summary: Invoke method ColSetDtlColumnChanged
   OperationID: ColSetDtlColumnChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColSetDtlColumnChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColSetDtlColumnChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ColSetDtlColumnChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ColSetDtlColumnChanged", {
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
   Summary: Invoke method GetMinValueOfDecimals
   Description: Returns minimum value of decimals.
   OperationID: GetMinValueOfDecimals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMinValueOfDecimals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMinValueOfDecimals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMinValueOfDecimals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetMinValueOfDecimals", {
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
   Summary: Invoke method ExportLookupTbl
   Description: Export table(s) from Kinetic
   OperationID: ExportLookupTbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportLookupTbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLookupTbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportLookupTbl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ExportLookupTbl", {
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
   Summary: Invoke method ImportPcLookupTableExt
   Description: Main entry point for import files  from Kinetic
   OperationID: ImportPcLookupTableExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTableExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTableExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportPcLookupTableExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ImportPcLookupTableExt", {
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
   Summary: Invoke method ImportPcLookupTableFromCSV
   Description: Process CVS file to DataTable structure
   OperationID: ImportPcLookupTableFromCSV
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportPcLookupTableFromCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportPcLookupTableFromCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportPcLookupTableFromCSV(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ImportPcLookupTableFromCSV", {
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
   Summary: Invoke method ColSetIDColumnChanging
   OperationID: ColSetIDColumnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ColSetIDColumnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColSetIDColumnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ColSetIDColumnChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/ColSetIDColumnChanging", {
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
   Summary: Invoke method GetNewPcLookupTblHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupTblHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcLookupTblHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetNewPcLookupTblHed", {
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
   Summary: Invoke method GetNewPcLookupTblHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupTblHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcLookupTblHedAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetNewPcLookupTblHedAttch", {
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
   Summary: Invoke method GetNewPcLookupColSetHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupColSetHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupColSetHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupColSetHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcLookupColSetHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetNewPcLookupColSetHed", {
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
   Summary: Invoke method GetNewPcLookupColSetDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupColSetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupColSetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupColSetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcLookupColSetDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetNewPcLookupColSetDtl", {
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
   Summary: Invoke method GetNewPcLookupTblValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcLookupTblValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcLookupTblValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcLookupTblValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcLookupTblValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetNewPcLookupTblValues", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PcLookupTblSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcLookupColSetDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupColSetHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcLookupColSetHedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcLookupTblHedAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcLookupTblHedRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcLookupTblListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcLookupTblValuesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcLookupTblValuesRow[],
}

export interface Erp_Tablesets_PcLookupColSetDtlRow{
      /**  Company  */  
   "Company":string,
      /**  LookupTblID  */  
   "LookupTblID":string,
      /**  ColSetID  */  
   "ColSetID":string,
      /**  ColName  */  
   "ColName":string,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  DataType  */  
   "DataType":string,
      /**  ColFormat  */  
   "ColFormat":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  AllowNegative  */  
   "AllowNegative":boolean,
      /**  NumericOnly  */  
   "NumericOnly":boolean,
      /**  UseSeparator  */  
   "UseSeparator":boolean,
      /**  Digits  */  
   "Digits":number,
      /**  Decimals  */  
   "Decimals":number,
   "DisplayFormat":string,
   "StringDigits":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcLookupColSetHedRow{
      /**  Company  */  
   "Company":string,
      /**  LookupTblID  */  
   "LookupTblID":string,
      /**  ColSetID  */  
   "ColSetID":string,
      /**  Description  */  
   "Description":string,
      /**  Template  */  
   "Template":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "UsedExternally":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcLookupTblHedAttchRow{
   "Company":string,
   "LookupTblID":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcLookupTblHedRow{
      /**  Company  */  
   "Company":string,
      /**  LookupTblID  */  
   "LookupTblID":string,
      /**  Description  */  
   "Description":string,
      /**  GlobalLookup  */  
   "GlobalLookup":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Indicates if Lookup table is global (master or link)  */  
   "GlbFlag":boolean,
   "EnableGlobalLookup":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcLookupTblListRow{
      /**  Company  */  
   "Company":string,
      /**  LookupTblID  */  
   "LookupTblID":string,
      /**  Description  */  
   "Description":string,
      /**  GlobalLookup  */  
   "GlobalLookup":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcLookupTblValuesRow{
      /**  Company  */  
   "Company":string,
      /**  LookupTblID  */  
   "LookupTblID":string,
      /**  RowNum  */  
   "RowNum":number,
      /**  ColName  */  
   "ColName":string,
      /**  ColSetID  */  
   "ColSetID":string,
      /**  RowSetID  */  
   "RowSetID":string,
      /**  DataValue  */  
   "DataValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  DataValueDecimal  */  
   "DataValueDecimal":number,
      /**  DataValueBool  */  
   "DataValueBool":boolean,
      /**  DataValueDate  */  
   "DataValueDate":string,
      /**  DataValueString  */  
   "DataValueString":string,
   "DataType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface ColSetDtlColumnChanged_input{
   proposedValue:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface ColSetDtlColumnChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface ColSetIDColumnChanging_input{
   proposedValue:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface ColSetIDColumnChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param sourceLookupTblID
      @param sourceColSetID
      @param destLookupTblID
      @param ds
   */  
export interface CopyColSet_input{
   sourceLookupTblID:string,
   sourceColSetID:string,
   destLookupTblID:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface CopyColSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param lookupTblID
   */  
export interface DeleteByID_input{
   lookupTblID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param lookupTblID
      @param rowNum
   */  
export interface DeleteLookupTblValue_input{
   lookupTblID:string,
   rowNum:number,
}

export interface DeleteLookupTblValue_output{
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
      /**  The actual generic table name used by the BL  */  
   DataTableID:string,
      /**  Unique identifier for the virtual schema  */  
   UniqueTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcLookupColSetDtlRow{
      /**  Company  */  
   Company:string,
      /**  LookupTblID  */  
   LookupTblID:string,
      /**  ColSetID  */  
   ColSetID:string,
      /**  ColName  */  
   ColName:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  DataType  */  
   DataType:string,
      /**  ColFormat  */  
   ColFormat:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  AllowNegative  */  
   AllowNegative:boolean,
      /**  NumericOnly  */  
   NumericOnly:boolean,
      /**  UseSeparator  */  
   UseSeparator:boolean,
      /**  Digits  */  
   Digits:number,
      /**  Decimals  */  
   Decimals:number,
   DisplayFormat:string,
   StringDigits:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcLookupColSetHedRow{
      /**  Company  */  
   Company:string,
      /**  LookupTblID  */  
   LookupTblID:string,
      /**  ColSetID  */  
   ColSetID:string,
      /**  Description  */  
   Description:string,
      /**  Template  */  
   Template:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   UsedExternally:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcLookupImportExportTableset{
   PcLookupTblHed:Erp_Tablesets_PcLookupTblHedRow[],
   PcLookupColSetDtl:Erp_Tablesets_PcLookupColSetDtlRow[],
   PcLookupColSetHed:Erp_Tablesets_PcLookupColSetHedRow[],
   PcLookupTblValues:Erp_Tablesets_PcLookupTblValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcLookupTblDispColumnsRow{
   ColSetID:string,
   ColumnFormat:string,
   ColumnName:string,
   ColumnSequence:number,
   ColumnType:string,
      /**  The ID of the Lookup Table.  */  
   LookupTblID:string,
   Digits:number,
   Decimals:number,
   AllowNegatives:boolean,
   UseSeparator:boolean,
   NumericOnly:boolean,
   StringDigits:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcLookupTblDisplayTableset{
   PcLookupTblDispColumns:Erp_Tablesets_PcLookupTblDispColumnsRow[],
   PcLookupTblValues:Erp_Tablesets_PcLookupTblValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcLookupTblHedAttchRow{
   Company:string,
   LookupTblID:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcLookupTblHedRow{
      /**  Company  */  
   Company:string,
      /**  LookupTblID  */  
   LookupTblID:string,
      /**  Description  */  
   Description:string,
      /**  GlobalLookup  */  
   GlobalLookup:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates if Lookup table is global (master or link)  */  
   GlbFlag:boolean,
   EnableGlobalLookup:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcLookupTblListRow{
      /**  Company  */  
   Company:string,
      /**  LookupTblID  */  
   LookupTblID:string,
      /**  Description  */  
   Description:string,
      /**  GlobalLookup  */  
   GlobalLookup:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcLookupTblListTableset{
   PcLookupTblList:Erp_Tablesets_PcLookupTblListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcLookupTblTableset{
   PcLookupTblHed:Erp_Tablesets_PcLookupTblHedRow[],
   PcLookupTblHedAttch:Erp_Tablesets_PcLookupTblHedAttchRow[],
   PcLookupColSetHed:Erp_Tablesets_PcLookupColSetHedRow[],
   PcLookupColSetDtl:Erp_Tablesets_PcLookupColSetDtlRow[],
   PcLookupTblValues:Erp_Tablesets_PcLookupTblValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcLookupTblValuesRow{
      /**  Company  */  
   Company:string,
      /**  LookupTblID  */  
   LookupTblID:string,
      /**  RowNum  */  
   RowNum:number,
      /**  ColName  */  
   ColName:string,
      /**  ColSetID  */  
   ColSetID:string,
      /**  RowSetID  */  
   RowSetID:string,
      /**  DataValue  */  
   DataValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  DataValueDecimal  */  
   DataValueDecimal:number,
      /**  DataValueBool  */  
   DataValueBool:boolean,
      /**  DataValueDate  */  
   DataValueDate:string,
      /**  DataValueString  */  
   DataValueString:string,
   DataType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPcLookupTblTableset{
   PcLookupTblHed:Erp_Tablesets_PcLookupTblHedRow[],
   PcLookupTblHedAttch:Erp_Tablesets_PcLookupTblHedAttchRow[],
   PcLookupColSetHed:Erp_Tablesets_PcLookupColSetHedRow[],
   PcLookupColSetDtl:Erp_Tablesets_PcLookupColSetDtlRow[],
   PcLookupTblValues:Erp_Tablesets_PcLookupTblValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param lookupTblID
      @param fileName
      @param fileType
   */  
export interface ExportLookupTbl_input{
      /**  One ID or delimited list of IDs for export.  */  
   lookupTblID:string,
      /**  Empty or subfolders of UserData server special folder  */  
   fileName:string,
      /**  xml or csv  */  
   fileType:string,
}

export interface ExportLookupTbl_output{
   returnObj:Erp_Tablesets_PcLookupImportExportTableset[],
parameters : {
      /**  output parameters  */  
   outMessage:string,
}
}

   /** Required : 
      @param lookupTblID
   */  
export interface GetByID_input{
   lookupTblID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PcLookupTblTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PcLookupTblTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PcLookupTblTableset[],
}

   /** Required : 
      @param lookupTblID
   */  
export interface GetDataTable_input{
   lookupTblID:string,
}

export interface GetDataTable_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param inLookupTblID
   */  
export interface GetDisplayColumns_input{
      /**  The LookupTbl ID  */  
   inLookupTblID:string,
}

export interface GetDisplayColumns_output{
   returnObj:Erp_Tablesets_PcLookupTblDisplayTableset[],
}

   /** Required : 
      @param pcLookupTblID
   */  
export interface GetExportPcLookupTables_input{
      /**  The PcLookupTbl Ids  */  
   pcLookupTblID:string,
}

export interface GetExportPcLookupTables_output{
   returnObj:Erp_Tablesets_PcLookupImportExportTableset[],
}

   /** Required : 
      @param optionType
   */  
export interface GetFormatOptions_input{
      /**  The type of option to get.
             Valid values are: NumberFormats, PriceMultipliers,
             SmartStringDateFormats, SmartStringDateSeparators, SmartStringLogicalFormats, NumFormatSignOptions, HTMLProducts  */  
   optionType:string,
}

export interface GetFormatOptions_output{
parameters : {
      /**  output parameters  */  
   optionList:string,
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
   returnObj:Erp_Tablesets_PcLookupTblListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetMinValueOfDecimals_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface GetMinValueOfDecimals_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param ds
      @param lookupTblID
      @param colSetID
   */  
export interface GetNewPcLookupColSetDtl_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
   lookupTblID:string,
   colSetID:string,
}

export interface GetNewPcLookupColSetDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param ds
      @param lookupTblID
   */  
export interface GetNewPcLookupColSetHed_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
   lookupTblID:string,
}

export interface GetNewPcLookupColSetHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param lookupTblID
      @param colSetID
   */  
export interface GetNewPcLookupTblDisplay_input{
   lookupTblID:string,
   colSetID:string,
}

export interface GetNewPcLookupTblDisplay_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param ds
      @param lookupTblID
   */  
export interface GetNewPcLookupTblHedAttch_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
   lookupTblID:string,
}

export interface GetNewPcLookupTblHedAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPcLookupTblHed_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface GetNewPcLookupTblHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param ds
      @param lookupTblID
      @param rowNum
   */  
export interface GetNewPcLookupTblValues_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
   lookupTblID:string,
   rowNum:number,
}

export interface GetNewPcLookupTblValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param whereClausePcLookupTblHed
      @param whereClausePcLookupTblHedAttch
      @param whereClausePcLookupColSetHed
      @param whereClausePcLookupColSetDtl
      @param whereClausePcLookupTblValues
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcLookupTblHed:string,
   whereClausePcLookupTblHedAttch:string,
   whereClausePcLookupColSetHed:string,
   whereClausePcLookupColSetDtl:string,
   whereClausePcLookupTblValues:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PcLookupTblTableset[],
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
      @param files
      @param processOption
      @param columnOption
      @param valuesOption
      @param ds
   */  
export interface ImportPcLookupTableExt_input{
   files:string,
   processOption:string,
   columnOption:string,
   valuesOption:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface ImportPcLookupTableExt_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param fileName
      @param processOption
      @param columnOption
      @param valuesOption
      @param ds
   */  
export interface ImportPcLookupTableFromCSV_input{
   fileName:string,
   processOption:string,
   columnOption:string,
   valuesOption:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface ImportPcLookupTableFromCSV_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param columnOption
      @param valuesOption
      @param dataSet
      @param lookupTblID
      @param lookupTblDesc
      @param lookupTblGlobalLookup
      @param lookupTblGlobalLock
      @param colSetID
      @param colSetDesc
      @param colSetTemplate
   */  
export interface ImportPcLookupTblFromCSV_input{
   columnOption:string,
   valuesOption:string,
   dataSet:any,      //schema had no properties on an object.
   lookupTblID:string,
   lookupTblDesc:string,
   lookupTblGlobalLookup:boolean,
   lookupTblGlobalLock:boolean,
   colSetID:string,
   colSetDesc:string,
   colSetTemplate:boolean,
}

export interface ImportPcLookupTblFromCSV_output{
}

   /** Required : 
      @param columnOption
      @param valuesOption
      @param ttPcLookupImportExportDS
      @param lookupTblID
      @param colsetID
   */  
export interface ImportPcLookupTbl_input{
   columnOption:string,
   valuesOption:string,
   ttPcLookupImportExportDS:Erp_Tablesets_PcLookupImportExportTableset[],
   lookupTblID:string,
   colsetID:string,
}

export interface ImportPcLookupTbl_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPcLookupTblTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPcLookupTblTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param lookupTblID
      @param colSetID
      @param rowNum
      @param colName
      @param proposedValue
      @param rowGuid
      @param ds
   */  
export interface UpdateLookupTblValue_input{
   lookupTblID:string,
   colSetID:string,
   rowNum:number,
   colName:string,
   proposedValue:string,
   rowGuid:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface UpdateLookupTblValue_output{
parameters : {
      /**  output parameters  */  
   rowGuid:string,
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PcLookupTblTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcLookupTblTableset[],
}
}

