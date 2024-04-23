import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DashBoardSvc
# Description: The DashBoard server logic.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DashBoards items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBoards
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards",headers=creds) as resp:
           return await resp.json()

async def post_DashBoards(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBoards
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DashBdDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBoard item
   Description: Calls GetByID to retrieve the DashBoard item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBoard
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DashBoard for the service
   Description: Calls UpdateExt to update DashBoard. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBoard
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DashBoard item
   Description: Call UpdateExt to delete DashBoard item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBoard
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdBAQs(Company, ProductID, GlbCompany, CGCCode, DefinitionID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DashBdBAQs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DashBdBAQs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdBAQs",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdBAQ item
   Description: Calls GetByID to retrieve the DashBdBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdBAQ1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdChunks(Company, ProductID, GlbCompany, CGCCode, DefinitionID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DashBdChunks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DashBdChunks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdChunkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdChunks",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company, ProductID, GlbCompany, CGCCode, DefinitionID, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdChunk item
   Description: Calls GetByID to retrieve the DashBdChunk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdChunk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdLikes(Company, ProductID, GlbCompany, CGCCode, DefinitionID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DashBdLikes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DashBdLikes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdLikes",headers=creds) as resp:
           return await resp.json()

async def get_DashBoards_Company_ProductID_GlbCompany_CGCCode_DefinitionID_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company, ProductID, GlbCompany, CGCCode, DefinitionID, LikeField, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdLike item
   Description: Calls GetByID to retrieve the DashBdLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdLike1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBoards(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + ")/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBdBAQs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DashBdBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdBAQs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs",headers=creds) as resp:
           return await resp.json()

async def post_DashBdBAQs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdBAQs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdBAQ item
   Description: Calls GetByID to retrieve the DashBdBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DashBdBAQ for the service
   Description: Calls UpdateExt to update DashBdBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DashBdBAQs_Company_ProductID_GlbCompany_CGCCode_DefinitionID_QueryID(Company, ProductID, GlbCompany, CGCCode, DefinitionID, QueryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DashBdBAQ item
   Description: Call UpdateExt to delete DashBdBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdBAQs(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBdChunks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DashBdChunks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdChunks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdChunkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks",headers=creds) as resp:
           return await resp.json()

async def post_DashBdChunks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdChunks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company, ProductID, GlbCompany, CGCCode, DefinitionID, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdChunk item
   Description: Calls GetByID to retrieve the DashBdChunk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdChunk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company, ProductID, GlbCompany, CGCCode, DefinitionID, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DashBdChunk for the service
   Description: Calls UpdateExt to update DashBdChunk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdChunk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdChunkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DashBdChunks_Company_ProductID_GlbCompany_CGCCode_DefinitionID_SeqNum(Company, ProductID, GlbCompany, CGCCode, DefinitionID, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DashBdChunk item
   Description: Call UpdateExt to delete DashBdChunk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdChunk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdChunks(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DashBdLikes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DashBdLikes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DashBdLikes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes",headers=creds) as resp:
           return await resp.json()

async def post_DashBdLikes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DashBdLikes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company, ProductID, GlbCompany, CGCCode, DefinitionID, LikeField, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DashBdLike item
   Description: Calls GetByID to retrieve the DashBdLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DashBdLike
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company, ProductID, GlbCompany, CGCCode, DefinitionID, LikeField, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DashBdLike for the service
   Description: Calls UpdateExt to update DashBdLike. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DashBdLike
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DashBdLikeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DashBdLikes_Company_ProductID_GlbCompany_CGCCode_DefinitionID_LikeField(Company, ProductID, GlbCompany, CGCCode, DefinitionID, LikeField, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DashBdLike item
   Description: Call UpdateExt to delete DashBdLike item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DashBdLike
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/DashBdLikes(" + Company + "," + ProductID + "," + GlbCompany + "," + CGCCode + "," + DefinitionID + "," + LikeField + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DashBdDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDashBdDef, whereClauseDashBdBAQ, whereClauseDashBdChunk, whereClauseDashBdLike, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDashBdDef=" + whereClauseDashBdDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDashBdBAQ=" + whereClauseDashBdBAQ
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDashBdChunk=" + whereClauseDashBdChunk
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDashBdLike=" + whereClauseDashBdLike
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, productID, glbCompany, cgCCode, definitionID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "productID=" + productID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "cgCCode=" + cgCCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "definitionID=" + definitionID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSourceCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSourceCompany
   Description: Get the source company for any Global Dashboard that is in the same tenant
   OperationID: GetSourceCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourceCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDashboardVersionInTenant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDashboardVersionInTenant
   Description: This method will get the DashBdVersion
   OperationID: GetDashboardVersionInTenant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDashboardVersionInTenant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardVersionInTenant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyHyphenInId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyHyphenInId
   Description: verify the DashboardId  make sure no rows match where hyphen in same position as underscore
   OperationID: VerifyHyphenInId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyHyphenInId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyHyphenInId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDashboardAssemblyInTenant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDashboardAssemblyInTenant
   Description: This method returns the FIRST Dashboard that HasAssembly that is also in the current tenant
first will invoke GetByID() looking for direct hit in current company,
else will find the first dashboard by definitionID in the collection of AssociatedCompanies
   OperationID: GetDashboardAssemblyInTenant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDashboardAssemblyInTenant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardAssemblyInTenant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDashboardsWithBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDashboardsWithBAQ
   Description: This methods returns a "list" dataset with possible DashBdDef records that match the current company,
inputted product identifier and inputted query identifier for each DashBdBAQ record.
   OperationID: GetDashboardsWithBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDashboardsWithBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardsWithBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDashboardsWithLike(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDashboardsWithLike
   Description: This methods returns a "list" dataset with possible DashBdDef records that match the current company (or are visible to all companies),
product identifier and like field for each DashBdLike record.
   OperationID: GetDashboardsWithLike
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDashboardsWithLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardsWithLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDashboardsRecs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDashboardsRecs
   Description: This methods returns a "list" dataset with possible DashBdDef records that match the current company,
inputted product identifier and inputted like field for each DashBdLike record.
   OperationID: GetDashboardsRecs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDashboardsRecs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDashboardsRecs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllCompaniesDashboard(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllCompaniesDashboard
   Description: Returns company id when there exists an AllCompanies Dashboard on different Company using the same DefinitionID
   OperationID: GetAllCompaniesDashboard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllCompaniesDashboard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllCompaniesDashboard_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StoreData(requestBody, epicorHeaders = None):
   """  
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StoreData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StoreData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDashBdDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDashBdDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDashBdDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDashBdBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDashBdBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDashBdBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDashBdChunk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDashBdChunk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdChunk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDashBdChunk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdChunk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDashBdLike(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDashBdLike
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDashBdLike
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDashBdLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDashBdLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DashBoardSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashBdBAQRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdChunkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashBdChunkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashBdDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashBdDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DashBdLikeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DashBdLikeRow] = obj["value"]
      pass

class Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.QueryID:str = obj["QueryID"]
      """  Query ID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdChunkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Chunk Sequence Number.  """  
      self.Chunk:str = obj["Chunk"]
      """  Contains a "Chunk" of data.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.Deployed:bool = obj["Deployed"]
      """  Deployed  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.WebAccess:bool = obj["WebAccess"]
      """  WebAccess  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.HasDashboardAssembly:bool = obj["HasDashboardAssembly"]
      """  HasDashboardAssembly  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.DashboardSchema:str = obj["DashboardSchema"]
      """  DashboardSchema  """  
      self.DashboardAssembly:str = obj["DashboardAssembly"]
      """  DashboardAssembly  """  
      self.WebAccess:bool = obj["WebAccess"]
      """  WebAccess  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.HasDashboardAssembly:bool = obj["HasDashboardAssembly"]
      """  HasDashboardAssembly  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdLikeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.LikeField:str = obj["LikeField"]
      """  Like Field  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   company
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetAllCompaniesDashboard_input:
   """ Required : 
   company
   product
   cgcCode
   definitionId
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.product:str = obj["product"]
      self.cgcCode:str = obj["cgcCode"]
      self.definitionId:str = obj["definitionId"]
      pass

class GetAllCompaniesDashboard_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBoardTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBoardTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBoardTableset] = obj["returnObj"]
      pass

class GetDashboardAssemblyInTenant_input:
   """ Required : 
   companyId
   ipProductId
   ipDefinitionId
   """  
   def __init__(self, obj):
      self.companyId:str = obj["companyId"]
      self.ipProductId:str = obj["ipProductId"]
      self.ipDefinitionId:str = obj["ipDefinitionId"]
      pass

class GetDashboardAssemblyInTenant_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBoardTableset] = obj["returnObj"]
      pass

class GetDashboardVersionInTenant_input:
   """ Required : 
   company
   productID
   definitionID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetDashboardVersionInTenant_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDashboardsRecs_input:
   """ Required : 
   ipDefinitionID
   ipProductId
   """  
   def __init__(self, obj):
      self.ipDefinitionID:str = obj["ipDefinitionID"]
      """  The Dashboard identifier.  """  
      self.ipProductId:str = obj["ipProductId"]
      """  The product identifier to return data for.  """  
      pass

class GetDashboardsRecs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opListID:str = obj["parameters"]
      self.opListGlobal:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDashboardsWithBAQ_input:
   """ Required : 
   ipProductId
   ipQueryID
   """  
   def __init__(self, obj):
      self.ipProductId:str = obj["ipProductId"]
      """  The product identifier to return data for.  """  
      self.ipQueryID:str = obj["ipQueryID"]
      """  The query identifier to return data for.  """  
      pass

class GetDashboardsWithBAQ_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBdDefListTableset] = obj["returnObj"]
      pass

class GetDashboardsWithLike_input:
   """ Required : 
   productId
   likeField
   """  
   def __init__(self, obj):
      self.productId:str = obj["productId"]
      """  The product identifier to return data for.  """  
      self.likeField:str = obj["likeField"]
      """  The like field to return data for.  """  
      pass

class GetDashboardsWithLike_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBdDefListTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBdDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDashBdBAQ_input:
   """ Required : 
   ds
   company
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewDashBdBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDashBdChunk_input:
   """ Required : 
   ds
   company
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewDashBdChunk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDashBdDef_input:
   """ Required : 
   ds
   company
   productID
   glbCompany
   cgCCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      pass

class GetNewDashBdDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDashBdLike_input:
   """ Required : 
   ds
   company
   productID
   glbCompany
   cgCCode
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.productID:str = obj["productID"]
      self.glbCompany:str = obj["glbCompany"]
      self.cgCCode:str = obj["cgCCode"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewDashBdLike_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDashBdDef
   whereClauseDashBdBAQ
   whereClauseDashBdChunk
   whereClauseDashBdLike
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDashBdDef:str = obj["whereClauseDashBdDef"]
      self.whereClauseDashBdBAQ:str = obj["whereClauseDashBdBAQ"]
      self.whereClauseDashBdChunk:str = obj["whereClauseDashBdChunk"]
      self.whereClauseDashBdLike:str = obj["whereClauseDashBdLike"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DashBoardTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSourceCompany_input:
   """ Required : 
   ipProductId
   ipDefinitionId
   """  
   def __init__(self, obj):
      self.ipProductId:str = obj["ipProductId"]
      self.ipDefinitionId:str = obj["ipDefinitionId"]
      pass

class GetSourceCompany_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Ice_Tablesets_DashBdBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.QueryID:str = obj["QueryID"]
      """  Query ID  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdChunkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Chunk Sequence Number.  """  
      self.Chunk:str = obj["Chunk"]
      """  Contains a "Chunk" of data.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.Deployed:bool = obj["Deployed"]
      """  Deployed  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.WebAccess:bool = obj["WebAccess"]
      """  WebAccess  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.HasDashboardAssembly:bool = obj["HasDashboardAssembly"]
      """  HasDashboardAssembly  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdDefListTableset:
   def __init__(self, obj):
      self.DashBdDefList:list[Ice_Tablesets_DashBdDefListRow] = obj["DashBdDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DashBdDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Last Updated Date  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Update By  """  
      self.DashBdVersion:str = obj["DashBdVersion"]
      """  Dashboard Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.Delivered:bool = obj["Delivered"]
      """  Indicates this dashboard is a system dashboard and any changes will be wiped with the next service pack.  """  
      self.MobileAccess:bool = obj["MobileAccess"]
      """  Indicates whether this Dashboard is available on the mobile menu.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.LastDeployedDate:str = obj["LastDeployedDate"]
      """  LastDeployedDate  """  
      self.LastDeployedBy:str = obj["LastDeployedBy"]
      """  LastDeployedBy  """  
      self.DashboardSchema:str = obj["DashboardSchema"]
      """  DashboardSchema  """  
      self.DashboardAssembly:str = obj["DashboardAssembly"]
      """  DashboardAssembly  """  
      self.WebAccess:bool = obj["WebAccess"]
      """  WebAccess  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Caption:str = obj["Caption"]
      """  Caption  """  
      self.HasDashboardAssembly:bool = obj["HasDashboardAssembly"]
      """  HasDashboardAssembly  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBdLikeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in identify from whch company this BAQ originated.  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  Dashboard Definition ID  """  
      self.LikeField:str = obj["LikeField"]
      """  Like Field  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DashBoardTableset:
   def __init__(self, obj):
      self.DashBdDef:list[Ice_Tablesets_DashBdDefRow] = obj["DashBdDef"]
      self.DashBdBAQ:list[Ice_Tablesets_DashBdBAQRow] = obj["DashBdBAQ"]
      self.DashBdChunk:list[Ice_Tablesets_DashBdChunkRow] = obj["DashBdChunk"]
      self.DashBdLike:list[Ice_Tablesets_DashBdLikeRow] = obj["DashBdLike"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtDashBoardTableset:
   def __init__(self, obj):
      self.DashBdDef:list[Ice_Tablesets_DashBdDefRow] = obj["DashBdDef"]
      self.DashBdBAQ:list[Ice_Tablesets_DashBdBAQRow] = obj["DashBdBAQ"]
      self.DashBdChunk:list[Ice_Tablesets_DashBdChunkRow] = obj["DashBdChunk"]
      self.DashBdLike:list[Ice_Tablesets_DashBdLikeRow] = obj["DashBdLike"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class StoreData_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

class StoreData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDashBoardTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDashBoardTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DashBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VerifyHyphenInId_input:
   """ Required : 
   company
   productId
   cgcCode
   definitionId
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.productId:str = obj["productId"]
      self.cgcCode:str = obj["cgcCode"]
      self.definitionId:str = obj["definitionId"]
      pass

class VerifyHyphenInId_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

