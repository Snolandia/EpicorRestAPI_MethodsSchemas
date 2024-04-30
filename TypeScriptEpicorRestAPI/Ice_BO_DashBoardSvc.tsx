import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.DashBoardSvc
// Description: The DashBoard server logic.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/$metadata", {
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
   Description: Get DashBoards items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBoards
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdDefRow
   */  
export function get_DashBoards(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBoards
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.DashBdDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DashBoards(requestBody:Ice_Tablesets_DashBdDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards", {
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
   Summary: Calls GetByID to retrieve the DashBoard item
   Description: Calls GetByID to retrieve the DashBoard item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBoard
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdDefRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")", {
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
         resolve(data as Ice_Tablesets_DashBdDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DashBoard for the service
   Description: Calls UpdateExt to update DashBoard. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBoard
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, requestBody:Ice_Tablesets_DashBdDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")", {
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
   Summary: Call UpdateExt to delete DashBoard item
   Description: Call UpdateExt to delete DashBoard item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBoard
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")", {
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
   Description: Get DashBdBAQs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DashBdBAQs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdBAQRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdBAQs(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdBAQs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DashBdBAQ item
   Description: Calls GetByID to retrieve the DashBdBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdBAQ1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdBAQRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, QueryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")", {
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
         resolve(data as Ice_Tablesets_DashBdBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DashBdChunks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DashBdChunks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdChunkRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdChunks(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdChunkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdChunks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdChunkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DashBdChunk item
   Description: Calls GetByID to retrieve the DashBdChunk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdChunk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdChunkRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdChunkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")", {
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
         resolve(data as Ice_Tablesets_DashBdChunkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DashBdLikes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DashBdLikes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdLikeRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdLikes(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdLikes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DashBdLike item
   Description: Calls GetByID to retrieve the DashBdLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdLike1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdLikeRow
   */  
export function get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, LikeField:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")", {
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
         resolve(data as Ice_Tablesets_DashBdLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DashBdBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdBAQs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdBAQRow
   */  
export function get_DashBdBAQs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdBAQs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.DashBdBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DashBdBAQs(requestBody:Ice_Tablesets_DashBdBAQRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs", {
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
   Summary: Calls GetByID to retrieve the DashBdBAQ item
   Description: Calls GetByID to retrieve the DashBdBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdBAQRow
   */  
export function get_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, QueryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdBAQRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")", {
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
         resolve(data as Ice_Tablesets_DashBdBAQRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DashBdBAQ for the service
   Description: Calls UpdateExt to update DashBdBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, QueryID:string, requestBody:Ice_Tablesets_DashBdBAQRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")", {
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
   Summary: Call UpdateExt to delete DashBdBAQ item
   Description: Call UpdateExt to delete DashBdBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdBAQ
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, QueryID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")", {
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
   Description: Get DashBdChunks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdChunks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdChunkRow
   */  
export function get_DashBdChunks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdChunkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdChunkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdChunks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.DashBdChunkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DashBdChunks(requestBody:Ice_Tablesets_DashBdChunkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks", {
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
   Summary: Calls GetByID to retrieve the DashBdChunk item
   Description: Calls GetByID to retrieve the DashBdChunk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdChunk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdChunkRow
   */  
export function get_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdChunkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")", {
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
         resolve(data as Ice_Tablesets_DashBdChunkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DashBdChunk for the service
   Description: Calls UpdateExt to update DashBdChunk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdChunk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, SeqNum:string, requestBody:Ice_Tablesets_DashBdChunkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete DashBdChunk item
   Description: Call UpdateExt to delete DashBdChunk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdChunk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")", {
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
   Description: Get DashBdLikes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdLikes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdLikeRow
   */  
export function get_DashBdLikes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdLikes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.DashBdLikeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DashBdLikes(requestBody:Ice_Tablesets_DashBdLikeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes", {
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
   Summary: Calls GetByID to retrieve the DashBdLike item
   Description: Calls GetByID to retrieve the DashBdLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdLike
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DashBdLikeRow
   */  
export function get_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, LikeField:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DashBdLikeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")", {
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
         resolve(data as Ice_Tablesets_DashBdLikeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DashBdLike for the service
   Description: Calls UpdateExt to update DashBdLike. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdLike
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, LikeField:string, requestBody:Ice_Tablesets_DashBdLikeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")", {
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
   Summary: Call UpdateExt to delete DashBdLike item
   Description: Call UpdateExt to delete DashBdLike item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdLike
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProductID Desc: ProductID   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param CGCCode Desc: CGCCode   Required: True   Allow empty value : True
      @param DefinitionID Desc: DefinitionID   Required: True   Allow empty value : True
      @param LikeField Desc: LikeField   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company:string, ProductID:string, GlbCompany:string, CGCCode:string, DefinitionID:string, LikeField:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDashBdDef:string, whereClauseDashBdBAQ:string, whereClauseDashBdChunk:string, whereClauseDashBdLike:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDashBdDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDashBdDef=" + whereClauseDashBdDef
   }
   if(typeof whereClauseDashBdBAQ!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDashBdBAQ=" + whereClauseDashBdBAQ
   }
   if(typeof whereClauseDashBdChunk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDashBdChunk=" + whereClauseDashBdChunk
   }
   if(typeof whereClauseDashBdLike!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDashBdLike=" + whereClauseDashBdLike
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, productID:string, glbCompany:string, cgCCode:string, definitionID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof productID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "productID=" + productID
   }
   if(typeof glbCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCompany=" + glbCompany
   }
   if(typeof cgCCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cgCCode=" + cgCCode
   }
   if(typeof definitionID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "definitionID=" + definitionID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetByID" + params, {
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
   Summary: Invoke method GetSourceCompany
   Description: Get the source company for any Global Dashboard that is in the same tenant
   OperationID: GetSourceCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSourceCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSourceCompany(requestBody:GetSourceCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSourceCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetSourceCompany", {
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
         resolve(data as GetSourceCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDashboardVersionInTenant
   Description: This method will get the DashBdVersion
   OperationID: GetDashboardVersionInTenant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDashboardVersionInTenant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardVersionInTenant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDashboardVersionInTenant(requestBody:GetDashboardVersionInTenant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDashboardVersionInTenant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetDashboardVersionInTenant", {
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
         resolve(data as GetDashboardVersionInTenant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyHyphenInId
   Description: verify the DashboardId  make sure no rows match where hyphen in same position as underscore
   OperationID: VerifyHyphenInId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyHyphenInId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyHyphenInId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyHyphenInId(requestBody:VerifyHyphenInId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyHyphenInId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/VerifyHyphenInId", {
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
         resolve(data as VerifyHyphenInId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDashboardAssemblyInTenant
   Description: This method returns the FIRST Dashboard that HasAssembly that is also in the current tenant
first will invoke GetByID() looking for direct hit in current company,
else will find the first dashboard by definitionID in the collection of AssociatedCompanies
   OperationID: GetDashboardAssemblyInTenant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDashboardAssemblyInTenant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardAssemblyInTenant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDashboardAssemblyInTenant(requestBody:GetDashboardAssemblyInTenant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDashboardAssemblyInTenant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetDashboardAssemblyInTenant", {
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
         resolve(data as GetDashboardAssemblyInTenant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDashboardsWithBAQ
   Description: This methods returns a "list" dataset with possible DashBdDef records that match the current company,
inputted product identifier and inputted query identifier for each DashBdBAQ record.
   OperationID: GetDashboardsWithBAQ
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDashboardsWithBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardsWithBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDashboardsWithBAQ(requestBody:GetDashboardsWithBAQ_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDashboardsWithBAQ_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetDashboardsWithBAQ", {
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
         resolve(data as GetDashboardsWithBAQ_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDashboardsWithLike
   Description: This methods returns a "list" dataset with possible DashBdDef records that match the current company (or are visible to all companies),
product identifier and like field for each DashBdLike record.
   OperationID: GetDashboardsWithLike
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDashboardsWithLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardsWithLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDashboardsWithLike(requestBody:GetDashboardsWithLike_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDashboardsWithLike_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetDashboardsWithLike", {
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
         resolve(data as GetDashboardsWithLike_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDashboardsRecs
   Description: This methods returns a "list" dataset with possible DashBdDef records that match the current company,
inputted product identifier and inputted like field for each DashBdLike record.
   OperationID: GetDashboardsRecs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDashboardsRecs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardsRecs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDashboardsRecs(requestBody:GetDashboardsRecs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDashboardsRecs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetDashboardsRecs", {
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
         resolve(data as GetDashboardsRecs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllCompaniesDashboard
   Description: Returns company id when there exists an AllCompanies Dashboard on different Company using the same DefinitionID
   OperationID: GetAllCompaniesDashboard
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllCompaniesDashboard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllCompaniesDashboard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllCompaniesDashboard(requestBody:GetAllCompaniesDashboard_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllCompaniesDashboard_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetAllCompaniesDashboard", {
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
         resolve(data as GetAllCompaniesDashboard_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method StoreData
   Description: This methods should be ran instead of the base Update method.
This method will require the dataset to come in, next it will delete all DashBdChunk,
DashBdBAQ, DashBdLike records associated with each ttDashBdDef in the dataset while also deleting
the DashBdDef records in the database.  Next the ttDashBdDef table will be the driving force behind
the creation of new DashBdDef, DashBdChunk, DashBdBAQ, and DashBdLike records in the database.
The values for the fields in these records will come from what is in the dataset.
This 'StoreData' process is basically a complete 'overlay' of the DashBoard data.
This method will require that all dataset records have a value of 'A' in the corresponding
SysRowId field/column.
   OperationID: StoreData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/StoreData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StoreData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StoreData(requestBody:StoreData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<StoreData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/StoreData", {
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
         resolve(data as StoreData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDashBdDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDashBdDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDashBdDef(requestBody:GetNewDashBdDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDashBdDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetNewDashBdDef", {
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
         resolve(data as GetNewDashBdDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDashBdBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdBAQ
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDashBdBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDashBdBAQ(requestBody:GetNewDashBdBAQ_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDashBdBAQ_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetNewDashBdBAQ", {
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
         resolve(data as GetNewDashBdBAQ_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDashBdChunk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdChunk
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDashBdChunk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdChunk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDashBdChunk(requestBody:GetNewDashBdChunk_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDashBdChunk_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetNewDashBdChunk", {
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
         resolve(data as GetNewDashBdChunk_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewDashBdLike
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdLike
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewDashBdLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDashBdLike(requestBody:GetNewDashBdLike_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewDashBdLike_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetNewDashBdLike", {
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
         resolve(data as GetNewDashBdLike_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DashBdBAQRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdChunkRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DashBdChunkRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DashBdDefListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DashBdDefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdLikeRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DashBdLikeRow,
}

export interface Ice_Tablesets_DashBdBAQRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   "GlbCompany":string,
      /**  Dashboard Definition ID  */  
   "DefinitionID":string,
      /**  Query ID  */  
   "QueryID":string,
      /**  Country Group / Country Code for CSF  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_DashBdChunkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   "GlbCompany":string,
      /**  Dashboard Definition ID  */  
   "DefinitionID":string,
      /**  Chunk Sequence Number.  */  
   "SeqNum":number,
      /**  Contains a "Chunk" of data.  */  
   "Chunk":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Deployed  */  
   "Deployed":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_DashBdDefListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   "GlbCompany":string,
      /**  Dashboard Definition ID  */  
   "DefinitionID":string,
      /**  Description  */  
   "Description":string,
      /**  Last Updated Date  */  
   "LastUpdated":string,
      /**  Last Update By  */  
   "LastUpdatedBy":string,
      /**  Dashboard Version  */  
   "DashBdVersion":string,
      /**  Database Version  */  
   "DataBaseVersion":number,
      /**  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  */  
   "Delivered":boolean,
      /**  Indicates whether this Dashboard is available on the mobile menu.  */  
   "MobileAccess":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  LastDeployedDate  */  
   "LastDeployedDate":string,
      /**  LastDeployedBy  */  
   "LastDeployedBy":string,
      /**  WebAccess  */  
   "WebAccess":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Caption  */  
   "Caption":string,
      /**  HasDashboardAssembly  */  
   "HasDashboardAssembly":boolean,
   "AllCompanies":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_DashBdDefRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   "GlbCompany":string,
      /**  Dashboard Definition ID  */  
   "DefinitionID":string,
      /**  Description  */  
   "Description":string,
      /**  Last Updated Date  */  
   "LastUpdated":string,
      /**  Last Update By  */  
   "LastUpdatedBy":string,
      /**  Dashboard Version  */  
   "DashBdVersion":string,
      /**  Database Version  */  
   "DataBaseVersion":number,
      /**  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  */  
   "Delivered":boolean,
      /**  Indicates whether this Dashboard is available on the mobile menu.  */  
   "MobileAccess":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  LastDeployedDate  */  
   "LastDeployedDate":string,
      /**  LastDeployedBy  */  
   "LastDeployedBy":string,
      /**  DashboardSchema  */  
   "DashboardSchema":string,
      /**  DashboardAssembly  */  
   "DashboardAssembly":string,
      /**  WebAccess  */  
   "WebAccess":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Caption  */  
   "Caption":string,
      /**  HasDashboardAssembly  */  
   "HasDashboardAssembly":boolean,
   "AllCompanies":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_DashBdLikeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VN - Vantage, VS - Vista  */  
   "ProductID":string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   "GlbCompany":string,
      /**  Dashboard Definition ID  */  
   "DefinitionID":string,
      /**  Like Field  */  
   "LikeField":string,
      /**  Country Group / Country Code for CSF  */  
   "CGCCode":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
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
   /** Required : 
      @param company
      @param productID
      @param glbCompany
      @param cgCCode
      @param definitionID
   */  
export interface DeleteByID_input{
   company:string,
   productID:string,
   glbCompany:string,
   cgCCode:string,
   definitionID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param company
      @param product
      @param cgcCode
      @param definitionId
   */  
export interface GetAllCompaniesDashboard_input{
   company:string,
   product:string,
   cgcCode:string,
   definitionId:string,
}

export interface GetAllCompaniesDashboard_output{
   returnObj:string,
}

   /** Required : 
      @param company
      @param productID
      @param glbCompany
      @param cgCCode
      @param definitionID
   */  
export interface GetByID_input{
   company:string,
   productID:string,
   glbCompany:string,
   cgCCode:string,
   definitionID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_DashBoardTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_DashBoardTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_DashBoardTableset[],
}

   /** Required : 
      @param companyId
      @param ipProductId
      @param ipDefinitionId
   */  
export interface GetDashboardAssemblyInTenant_input{
   companyId:string,
   ipProductId:string,
   ipDefinitionId:string,
}

export interface GetDashboardAssemblyInTenant_output{
   returnObj:Ice_Tablesets_DashBoardTableset[],
}

   /** Required : 
      @param company
      @param productID
      @param definitionID
   */  
export interface GetDashboardVersionInTenant_input{
   company:string,
   productID:string,
   definitionID:string,
}

export interface GetDashboardVersionInTenant_output{
   returnObj:string,
}

   /** Required : 
      @param ipDefinitionID
      @param ipProductId
   */  
export interface GetDashboardsRecs_input{
      /**  The Dashboard identifier.  */  
   ipDefinitionID:string,
      /**  The product identifier to return data for.  */  
   ipProductId:string,
}

export interface GetDashboardsRecs_output{
parameters : {
      /**  output parameters  */  
   opListID:string,
   opListGlobal:string,
}
}

   /** Required : 
      @param ipProductId
      @param ipQueryID
   */  
export interface GetDashboardsWithBAQ_input{
      /**  The product identifier to return data for.  */  
   ipProductId:string,
      /**  The query identifier to return data for.  */  
   ipQueryID:string,
}

export interface GetDashboardsWithBAQ_output{
   returnObj:Ice_Tablesets_DashBdDefListTableset[],
}

   /** Required : 
      @param productId
      @param likeField
   */  
export interface GetDashboardsWithLike_input{
      /**  The product identifier to return data for.  */  
   productId:string,
      /**  The like field to return data for.  */  
   likeField:string,
}

export interface GetDashboardsWithLike_output{
   returnObj:Ice_Tablesets_DashBdDefListTableset[],
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
   returnObj:Ice_Tablesets_DashBdDefListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param productID
      @param glbCompany
      @param cgCCode
      @param definitionID
   */  
export interface GetNewDashBdBAQ_input{
   ds:Ice_Tablesets_DashBoardTableset[],
   company:string,
   productID:string,
   glbCompany:string,
   cgCCode:string,
   definitionID:string,
}

export interface GetNewDashBdBAQ_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DashBoardTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param productID
      @param glbCompany
      @param cgCCode
      @param definitionID
   */  
export interface GetNewDashBdChunk_input{
   ds:Ice_Tablesets_DashBoardTableset[],
   company:string,
   productID:string,
   glbCompany:string,
   cgCCode:string,
   definitionID:string,
}

export interface GetNewDashBdChunk_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DashBoardTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param productID
      @param glbCompany
      @param cgCCode
   */  
export interface GetNewDashBdDef_input{
   ds:Ice_Tablesets_DashBoardTableset[],
   company:string,
   productID:string,
   glbCompany:string,
   cgCCode:string,
}

export interface GetNewDashBdDef_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DashBoardTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param productID
      @param glbCompany
      @param cgCCode
      @param definitionID
   */  
export interface GetNewDashBdLike_input{
   ds:Ice_Tablesets_DashBoardTableset[],
   company:string,
   productID:string,
   glbCompany:string,
   cgCCode:string,
   definitionID:string,
}

export interface GetNewDashBdLike_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DashBoardTableset,
}
}

   /** Required : 
      @param whereClauseDashBdDef
      @param whereClauseDashBdBAQ
      @param whereClauseDashBdChunk
      @param whereClauseDashBdLike
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDashBdDef:string,
   whereClauseDashBdBAQ:string,
   whereClauseDashBdChunk:string,
   whereClauseDashBdLike:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_DashBoardTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipProductId
      @param ipDefinitionId
   */  
export interface GetSourceCompany_input{
   ipProductId:string,
   ipDefinitionId:string,
}

export interface GetSourceCompany_output{
   returnObj:string,
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

export interface Ice_Tablesets_DashBdBAQRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   GlbCompany:string,
      /**  Dashboard Definition ID  */  
   DefinitionID:string,
      /**  Query ID  */  
   QueryID:string,
      /**  Country Group / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DashBdChunkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   GlbCompany:string,
      /**  Dashboard Definition ID  */  
   DefinitionID:string,
      /**  Chunk Sequence Number.  */  
   SeqNum:number,
      /**  Contains a "Chunk" of data.  */  
   Chunk:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Deployed  */  
   Deployed:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DashBdDefListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   GlbCompany:string,
      /**  Dashboard Definition ID  */  
   DefinitionID:string,
      /**  Description  */  
   Description:string,
      /**  Last Updated Date  */  
   LastUpdated:string,
      /**  Last Update By  */  
   LastUpdatedBy:string,
      /**  Dashboard Version  */  
   DashBdVersion:string,
      /**  Database Version  */  
   DataBaseVersion:number,
      /**  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  */  
   Delivered:boolean,
      /**  Indicates whether this Dashboard is available on the mobile menu.  */  
   MobileAccess:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  LastDeployedDate  */  
   LastDeployedDate:string,
      /**  LastDeployedBy  */  
   LastDeployedBy:string,
      /**  WebAccess  */  
   WebAccess:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Caption  */  
   Caption:string,
      /**  HasDashboardAssembly  */  
   HasDashboardAssembly:boolean,
   AllCompanies:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DashBdDefListTableset{
   DashBdDefList:Ice_Tablesets_DashBdDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_DashBdDefRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   GlbCompany:string,
      /**  Dashboard Definition ID  */  
   DefinitionID:string,
      /**  Description  */  
   Description:string,
      /**  Last Updated Date  */  
   LastUpdated:string,
      /**  Last Update By  */  
   LastUpdatedBy:string,
      /**  Dashboard Version  */  
   DashBdVersion:string,
      /**  Database Version  */  
   DataBaseVersion:number,
      /**  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  */  
   Delivered:boolean,
      /**  Indicates whether this Dashboard is available on the mobile menu.  */  
   MobileAccess:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  LastDeployedDate  */  
   LastDeployedDate:string,
      /**  LastDeployedBy  */  
   LastDeployedBy:string,
      /**  DashboardSchema  */  
   DashboardSchema:string,
      /**  DashboardAssembly  */  
   DashboardAssembly:string,
      /**  WebAccess  */  
   WebAccess:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Caption  */  
   Caption:string,
      /**  HasDashboardAssembly  */  
   HasDashboardAssembly:boolean,
   AllCompanies:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DashBdLikeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VN - Vantage, VS - Vista  */  
   ProductID:string,
      /**  Global Company identifier.  Used in identify from whch company this BAQ originated.  */  
   GlbCompany:string,
      /**  Dashboard Definition ID  */  
   DefinitionID:string,
      /**  Like Field  */  
   LikeField:string,
      /**  Country Group / Country Code for CSF  */  
   CGCCode:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DashBoardTableset{
   DashBdDef:Ice_Tablesets_DashBdDefRow[],
   DashBdBAQ:Ice_Tablesets_DashBdBAQRow[],
   DashBdChunk:Ice_Tablesets_DashBdChunkRow[],
   DashBdLike:Ice_Tablesets_DashBdLikeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtDashBoardTableset{
   DashBdDef:Ice_Tablesets_DashBdDefRow[],
   DashBdBAQ:Ice_Tablesets_DashBdBAQRow[],
   DashBdChunk:Ice_Tablesets_DashBdChunkRow[],
   DashBdLike:Ice_Tablesets_DashBdLikeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface StoreData_input{
   ds:Ice_Tablesets_DashBoardTableset[],
}

export interface StoreData_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DashBoardTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtDashBoardTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtDashBoardTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_DashBoardTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DashBoardTableset,
}
}

   /** Required : 
      @param company
      @param productId
      @param cgcCode
      @param definitionId
   */  
export interface VerifyHyphenInId_input{
   company:string,
   productId:string,
   cgcCode:string,
   definitionId:string,
}

export interface VerifyHyphenInId_output{
   returnObj:string,
}

