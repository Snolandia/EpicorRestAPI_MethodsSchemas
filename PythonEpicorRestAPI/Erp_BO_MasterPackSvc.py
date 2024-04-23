import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MasterPackSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MasterPacks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPacks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks",headers=creds) as resp:
           return await resp.json()

async def post_MasterPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum(Company, PackNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPack item
   Description: Calls GetByID to retrieve the MasterPack item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPack
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MasterPacks_Company_PackNum(Company, PackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MasterPack for the service
   Description: Calls UpdateExt to update MasterPack. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPack
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MasterPacks_Company_PackNum(Company, PackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MasterPack item
   Description: Call UpdateExt to delete MasterPack item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPack
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum_MasterPackDtls(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MasterPackDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MasterPackDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackDtls",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum_MasterPackDtls_Company_MPackLine_DtlPackNum(Company, PackNum, MPackLine, DtlPackNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPackDtl item
   Description: Calls GetByID to retrieve the MasterPackDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param MPackLine: Desc: MPackLine   Required: True
      :param DtlPackNum: Desc: DtlPackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum_MasterPackUPS(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MasterPackUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MasterPackUPS1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackUPS",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum_MasterPackUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPackUP item
   Description: Calls GetByID to retrieve the MasterPackUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackUP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum_MasterPackAttches(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MasterPackAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MasterPackAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackAttches",headers=creds) as resp:
           return await resp.json()

async def get_MasterPacks_Company_PackNum_MasterPackAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPackAttch item
   Description: Calls GetByID to retrieve the MasterPackAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MasterPackDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MasterPackDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPackDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls",headers=creds) as resp:
           return await resp.json()

async def post_MasterPackDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPackDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MasterPackDtls_Company_MPackLine_DtlPackNum(Company, MPackLine, DtlPackNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPackDtl item
   Description: Calls GetByID to retrieve the MasterPackDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MPackLine: Desc: MPackLine   Required: True
      :param DtlPackNum: Desc: DtlPackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MasterPackDtls_Company_MPackLine_DtlPackNum(Company, MPackLine, DtlPackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MasterPackDtl for the service
   Description: Calls UpdateExt to update MasterPackDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPackDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MPackLine: Desc: MPackLine   Required: True
      :param DtlPackNum: Desc: DtlPackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MasterPackDtls_Company_MPackLine_DtlPackNum(Company, MPackLine, DtlPackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MasterPackDtl item
   Description: Call UpdateExt to delete MasterPackDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPackDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MPackLine: Desc: MPackLine   Required: True
      :param DtlPackNum: Desc: DtlPackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MasterPackUPS(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MasterPackUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPackUPS
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS",headers=creds) as resp:
           return await resp.json()

async def post_MasterPackUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPackUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MasterPackUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPackUP item
   Description: Calls GetByID to retrieve the MasterPackUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MasterPackUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MasterPackUP for the service
   Description: Calls UpdateExt to update MasterPackUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPackUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MasterPackUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MasterPackUP item
   Description: Call UpdateExt to delete MasterPackUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPackUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MasterPackAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MasterPackAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPackAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches",headers=creds) as resp:
           return await resp.json()

async def post_MasterPackAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPackAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MasterPackAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MasterPackAttch item
   Description: Calls GetByID to retrieve the MasterPackAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MasterPackAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MasterPackAttch for the service
   Description: Calls UpdateExt to update MasterPackAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPackAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MasterPackAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MasterPackAttch item
   Description: Call UpdateExt to delete MasterPackAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPackAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CartonDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CartonDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails",headers=creds) as resp:
           return await resp.json()

async def post_CartonDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CartonDetails_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonDetail item
   Description: Calls GetByID to retrieve the CartonDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonDetail
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CartonDetails_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CartonDetail for the service
   Description: Calls UpdateExt to update CartonDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonDetail
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CartonDetails_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CartonDetail item
   Description: Call UpdateExt to delete CartonDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonDetail
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterpackListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMasterPack, whereClauseMasterPackAttch, whereClauseMasterPackDtl, whereClauseMasterPackUPS, whereClauseCartonDetail, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMasterPack=" + whereClauseMasterPack
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMasterPackAttch=" + whereClauseMasterPackAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMasterPackDtl=" + whereClauseMasterPackDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMasterPackUPS=" + whereClauseMasterPackUPS
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCartonDetail=" + whereClauseCartonDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(packNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "packNum=" + packNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the miscellaneous shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateWeight
   Description: Purpose:  calculate the weight of a carton based upon Part.Weight.
<param name="ds">MasterpackDataSet</param><param name="weight">Pack Weight</param>
   OperationID: CalculateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelVoidCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelVoidCarton
   Description: Checks to see if the carton void can be cancelled and re-opens it if it is allowed.
   OperationID: CancelVoidCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelVoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelVoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearConvertedManifest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearConvertedManifest
   Description: Purpose: Clear TFShipHead Manifest fields when Unfreighting.
<param name="ipPackNum">Pack Num to clear Manifest fields</param>
Notes:
   OperationID: ClearConvertedManifest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseCarton
   Description: Checks to see if the carton can be closed and closes it if it is allowed.
   OperationID: CloseCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertToManifestUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertToManifestUOM
   Description: Purpose: Populate Masterpack Manifest fields.
<param name="ipPackNum">Pack Num to populate Manifest fields</param>
Notes:
   OperationID: ConvertToManifestUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetCustPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMiscPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMiscPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetMiscPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMiscPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMiscPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackaging
   Description: Purpose:
Parameters:
<param name="ipPkgCode">package code</param><param name="ds">Masterpack Shipment data set </param>
Notes:
   OperationID: GetPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackClass
   Description: Purpose:
Parameters:
<param name="ipPkgClass">package class</param><param name="ds">Masterpack Shipment data set </param>
Notes:
   OperationID: GetPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param><param name="ds">The Masterpack shipment data set </param>
Notes:
   OperationID: GetPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetScale(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetScale
   Description: Purpose: Retrieve workstation scale settings
Parameters:
<param name="workstationID">Workstation ID to retrieve scale settings </param><param name="ScaleID">Workstation default scale</param>
Notes:
   OperationID: GetScale
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipDetails
   Description: This method displays the shipto address information when the ShipToNum field changes
Should only be called on new Shipments or if the Shipment has no lines and if
the MultipleShippers flag is yes
   OperationID: GetShipDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSubPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSubPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetSubPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSubPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransferPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransferPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetTransferPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenCarton
   Description: Checks to see if the carton can be opened and opens it if it is allowed.
   OperationID: OpenCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessFreightInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessFreightInfo
   Description: Purpose: Update the freighted shipment
<param name="iPackNum">The carton number of the carton to open </param><param name="ds">Freight Response data set</param><returns>The Masterpack data set </returns>
Notes:
   OperationID: ProcessFreightInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessFreightInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFreightInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessUnFreightInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessUnFreightInfo
   Description: Purpose: Update the freighted shipment
<param name="iPackNum">The carton number of the carton to open </param><param name="opWarnMsg">Warning message the UI is to present to the user</param><returns>The Masterpack data set </returns>
Notes:
   OperationID: ProcessUnFreightInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessUnFreightInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessUnFreightInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVEnable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
Parameters:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The Masterpack data set </param>
Notes:
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVShipStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVShipStatus
   Description: Purpose:
Parameters:
<param name="ipShipStatus">Shipment status</param><param name="ds">The Masterpack shipment data set </param>
Notes:
   OperationID: SetUPSQVShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StageCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StageCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: StageCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StageCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StageCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateManifestChargeAmts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateManifestChargeAmts
   Description: Purpose:  Calculate the CODAmount or DeclaredAmt
Parameters:
<param name="ipAmountType">COD or DeclaredAmt</param><param name="ipAction">Yes = recalculate No = reset to zero</param><param name="ds">Masterpack Shipment data set </param>
Notes:  Update the COD Amount and/or Declared Insurance amounts for manifesting purposes.
   OperationID: UpdateManifestChargeAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateManifestChargeAmts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateManifestChargeAmts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: VoidCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CartonExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CartonExists
   OperationID: CartonExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CartonExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCartonInShip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCartonInShip
   OperationID: CheckCartonInShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCartonInShip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCartonInShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCartonStaged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCartonStaged
   OperationID: CheckCartonStaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCartonStaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCartonStaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckShipStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckShipStatus
   OperationID: CheckShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetListEnhanced(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListEnhanced
   Description: Purpose: Returns valid MasterPack Rows
Parameters:
<param name="ipType">type </param><param name="ipStatus">ipStatus</param><param name="ipSortBy">ipSortNy</param><param name="ipStartAtPackNum">ipStartAtPackNum</param><param name="ipStartAtShipDate">ipStartAtShipDate</param><param name="ipStartAtLegalNumber">ipStartAtLegalNumber</param><param name="ipShipViaCode">ipShipViaCode</param><param name="ipCustNum">ipCustNum</param><param name="ipShipToNum">ipShipToNum</param><param name="ipVendorNum">ipVendorNum</param><param name="pageSize">Page Size</param><param name="absolutePage">Absolute Page</param><param name="morePages">More Pages flag</param><returns>MasterpackListTableset dataset</returns>
Notes:
   OperationID: GetListEnhanced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListEnhanced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListEnhanced_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateDigitalSignature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMasterPack(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMasterPack
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPack
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPack_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPack_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMasterPackAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMasterPackAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPackAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPackAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPackAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMasterPackDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMasterPackDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPackDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPackDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPackDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMasterPackUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMasterPackUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPackUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPackUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPackUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CartonDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasterPackAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasterPackDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasterPackRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackUPSRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasterPackUPSRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterpackListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasterpackListRow] = obj["value"]
      pass

class Erp_Tablesets_CartonDetailRow:
   def __init__(self, obj):
      self.PackNum:int = obj["PackNum"]
      self.DtlPackNum:int = obj["DtlPackNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.PartNumber:str = obj["PartNumber"]
      self.Description:str = obj["Description"]
      self.PackQty:int = obj["PackQty"]
      self.QtyOrdered:int = obj["QtyOrdered"]
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.partAESExp:str = obj["partAESExp"]
      """  Used by the freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by the freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by the freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by the freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by the freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by the freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by the freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by the freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by the freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by the freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by the freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by the freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by the freight web service  """  
      self.PartSchedBCode:str = obj["PartSchedBCode"]
      """  Used by the freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by the freight web service  """  
      self.PackQtyUom:str = obj["PackQtyUom"]
      self.QtyOrderedUOM:str = obj["QtyOrderedUOM"]
      self.PackJobQty:int = obj["PackJobQty"]
      self.PackJobUom:str = obj["PackJobUom"]
      self.PackLine:int = obj["PackLine"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  AttributeSetID  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  ShortDescription  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the part  revision. Default from the RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Master pack packnum  """  
      self.DtlPackNum:int = obj["DtlPackNum"]
      """  Carton number of the detail.  Links to a shipment header record ShipHead, etc.  """  
      self.MPackLine:int = obj["MPackLine"]
      """  An integer that uniquely identifies a detail record within a Master Pack. This is assigned by the system. Read last MasterPackDtl record for PackNum and add 1.  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Used by the freight web service  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Used by the freight web service  """  
      self.ConCity:str = obj["ConCity"]
      """  Used by the freight web service  """  
      self.ConCompName:str = obj["ConCompName"]
      """  Used by the freight web service  """  
      self.ConContact:str = obj["ConContact"]
      """  Used by the freight web service  """  
      self.ConCountry:str = obj["ConCountry"]
      """  Used by the freight web service  """  
      self.ConPhoneNum:str = obj["ConPhoneNum"]
      """  Used by the freight web service  """  
      self.ConAddress1:str = obj["ConAddress1"]
      """  Used by the freight web service  """  
      self.ConAddress2:str = obj["ConAddress2"]
      """  Used by the freight web service  """  
      self.ConsigneeID:str = obj["ConsigneeID"]
      """  Used by the freight web service  """  
      self.ConState:str = obj["ConState"]
      """  Used by the freight web service  """  
      self.ConZip:str = obj["ConZip"]
      """  Used by the freight web service  """  
      self.CustPONumber:str = obj["CustPONumber"]
      """  Used by the freight web service  """  
      self.DropShip:bool = obj["DropShip"]
      """  Used by the freight web service  """  
      self.FFCity:str = obj["FFCity"]
      """  Used by the freight web service  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Used by the freight web service  """  
      self.FFContact:str = obj["FFContact"]
      """  Used by the freight web service  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Used by the freight web service  """  
      self.FFID:str = obj["FFID"]
      """  Used by the freight web service  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Used by the freight web service  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  Used by the freight web service  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Used by the freight web service  """  
      self.FFState:str = obj["FFState"]
      """  Used by the freight web service  """  
      self.FFZip:str = obj["FFZip"]
      """  Used by the freight web service  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Used by the freight web service  """  
      self.JobNumber:str = obj["JobNumber"]
      """  Used by the freight web service  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Used by the freight web service  """  
      self.OrderNum:str = obj["OrderNum"]
      """  Used by the freight web service  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Used by the freight web service  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Used by the freight web service  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Used by the freight web service  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Used by the freight web service  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Used by the freight web service  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Used by the freight web service  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Used by the freight web service  """  
      self.PayFlag:bool = obj["PayFlag"]
      """  Used by the freight web service  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Used by the freight web service  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Used by the freight web service  """  
      self.TotalOrderValueCurrencyUOM:str = obj["TotalOrderValueCurrencyUOM"]
      self.ShipmentTypeDesc:str = obj["ShipmentTypeDesc"]
      """  Readable translated description of ShipmentType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Inter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  This field is reserved for future development.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.BillToAddrList:str = obj["BillToAddrList"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates of TranDocTypeID is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the option to void the legal number is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Logical indicating to the UI that the weight prompt is to be enabled.  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration is setup for master pack  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height field is enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length field is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width field is enabled.  """  
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      self.AddrList:str = obj["AddrList"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if information on the master pack can be modified after the document has been printed.  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sumo of the value of the items in the carton  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  carton Length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if the option to assign a legal number is available.  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      """  Formatted address column for ShipTo field  """  
      self.SoldToAddrFormatted:str = obj["SoldToAddrFormatted"]
      """  Formatted address column for Sold To  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantity View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email adress to be used for notifications.  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the UPS Quantum View is to be enabled.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterpackListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Inter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  This field is reserved for future development.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton height  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.CartonLength:int = obj["CartonLength"]
      """  carton Length  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sumo of the value of the items in the carton  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height field is enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length field is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width field is enabled.  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Logical indicating to the UI that the weight prompt is to be enabled.  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if the option to assign a legal number is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the option to void the legal number is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration is setup for master pack  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if information on the master pack can be modified after the document has been printed.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates of TranDocTypeID is available for input  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.OurBankBankName:str = obj["OurBankBankName"]
      """  The Bank's full name.  """  
      self.OurBankDescription:str = obj["OurBankDescription"]
      """  Full description of the bank account.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalculateWeight_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class CalculateWeight_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.weight:int = obj["parameters"]
      pass

      """  output parameters  """  

class CancelVoidCarton_input:
   """ Required : 
   iPackNum
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to open  """  
      pass

class CancelVoidCarton_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

class CartonExists_input:
   """ Required : 
   packNum
   shipmentType
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.shipmentType:str = obj["shipmentType"]
      pass

class CartonExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckCartonInShip_input:
   """ Required : 
   packNum
   shipViaCode
   shipToNum
   shipmentType
   custNum
   masterPackNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.shipViaCode:str = obj["shipViaCode"]
      self.shipToNum:str = obj["shipToNum"]
      self.shipmentType:str = obj["shipmentType"]
      self.custNum:int = obj["custNum"]
      self.masterPackNum:int = obj["masterPackNum"]
      pass

class CheckCartonInShip_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckCartonStaged_input:
   """ Required : 
   packNum
   shipmentType
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.shipmentType:str = obj["shipmentType"]
      pass

class CheckCartonStaged_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckShipStatus_input:
   """ Required : 
   packNum
   shipmentType
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.shipmentType:str = obj["shipmentType"]
      pass

class CheckShipStatus_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ClearConvertedManifest_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ClearConvertedManifest_output:
   def __init__(self, obj):
      pass

class CloseCarton_input:
   """ Required : 
   iPackNum
   ds
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to close  """  
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class CloseCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertToManifestUOM_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ConvertToManifestUOM_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CartonDetailRow:
   def __init__(self, obj):
      self.PackNum:int = obj["PackNum"]
      self.DtlPackNum:int = obj["DtlPackNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.PartNumber:str = obj["PartNumber"]
      self.Description:str = obj["Description"]
      self.PackQty:int = obj["PackQty"]
      self.QtyOrdered:int = obj["QtyOrdered"]
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.partAESExp:str = obj["partAESExp"]
      """  Used by the freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by the freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by the freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by the freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by the freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by the freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by the freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by the freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by the freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by the freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by the freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by the freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by the freight web service  """  
      self.PartSchedBCode:str = obj["PartSchedBCode"]
      """  Used by the freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by the freight web service  """  
      self.PackQtyUom:str = obj["PackQtyUom"]
      self.QtyOrderedUOM:str = obj["QtyOrderedUOM"]
      self.PackJobQty:int = obj["PackJobQty"]
      self.PackJobUom:str = obj["PackJobUom"]
      self.PackLine:int = obj["PackLine"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  AttributeSetID  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  ShortDescription  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the part  revision. Default from the RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FreightCartonResponseRow:
   def __init__(self, obj):
      self.CallTagNumber:str = obj["CallTagNumber"]
      self.DimWeight:int = obj["DimWeight"]
      self.DimWeightUOM:str = obj["DimWeightUOM"]
      self.DiscountFreightAmount:int = obj["DiscountFreightAmount"]
      self.DiscountFreightAmountUOM:str = obj["DiscountFreightAmountUOM"]
      self.ErrorFlag:bool = obj["ErrorFlag"]
      self.ErrorMessage:str = obj["ErrorMessage"]
      self.EstimatedFreightAmount:int = obj["EstimatedFreightAmount"]
      self.EstimatedFreightAmountUOM:str = obj["EstimatedFreightAmountUOM"]
      self.EstimatedFreightFlag:bool = obj["EstimatedFreightFlag"]
      self.FreightZone:str = obj["FreightZone"]
      self.OtherAmount:int = obj["OtherAmount"]
      self.OtherAmountUOM:str = obj["OtherAmountUOM"]
      self.OversizeFlag:bool = obj["OversizeFlag"]
      self.PickupNumber:str = obj["PickupNumber"]
      self.PublishedFreightAmount:int = obj["PublishedFreightAmount"]
      self.PublishedFreightAmountUOM:str = obj["PublishedFreightAmountUOM"]
      self.ShipDate:str = obj["ShipDate"]
      self.TemplateCode:str = obj["TemplateCode"]
      self.TransactionNumber:str = obj["TransactionNumber"]
      self.WayBillNbr:str = obj["WayBillNbr"]
      self.FreightedShipVia:str = obj["FreightedShipVia"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FreightCartonResponseTrackingRow:
   def __init__(self, obj):
      self.TrackingNumber:str = obj["TrackingNumber"]
      self.PackID:int = obj["PackID"]
      self.DiscountFreightAmt:int = obj["DiscountFreightAmt"]
      """  Discounted freight amount calculated by the shipper  """  
      self.PublishedFreightAmt:int = obj["PublishedFreightAmt"]
      """  Published freight amount determined by the shipper.  """  
      self.CaseNum:str = obj["CaseNum"]
      """  Concatenation of the pack num and sequential case number.  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Shipment type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FreightInfoResponseTableset:
   def __init__(self, obj):
      self.FreightCartonResponse:list[Erp_Tablesets_FreightCartonResponseRow] = obj["FreightCartonResponse"]
      self.FreightCartonResponseTracking:list[Erp_Tablesets_FreightCartonResponseTrackingRow] = obj["FreightCartonResponseTracking"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Master pack packnum  """  
      self.DtlPackNum:int = obj["DtlPackNum"]
      """  Carton number of the detail.  Links to a shipment header record ShipHead, etc.  """  
      self.MPackLine:int = obj["MPackLine"]
      """  An integer that uniquely identifies a detail record within a Master Pack. This is assigned by the system. Read last MasterPackDtl record for PackNum and add 1.  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Used by the freight web service  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Used by the freight web service  """  
      self.ConCity:str = obj["ConCity"]
      """  Used by the freight web service  """  
      self.ConCompName:str = obj["ConCompName"]
      """  Used by the freight web service  """  
      self.ConContact:str = obj["ConContact"]
      """  Used by the freight web service  """  
      self.ConCountry:str = obj["ConCountry"]
      """  Used by the freight web service  """  
      self.ConPhoneNum:str = obj["ConPhoneNum"]
      """  Used by the freight web service  """  
      self.ConAddress1:str = obj["ConAddress1"]
      """  Used by the freight web service  """  
      self.ConAddress2:str = obj["ConAddress2"]
      """  Used by the freight web service  """  
      self.ConsigneeID:str = obj["ConsigneeID"]
      """  Used by the freight web service  """  
      self.ConState:str = obj["ConState"]
      """  Used by the freight web service  """  
      self.ConZip:str = obj["ConZip"]
      """  Used by the freight web service  """  
      self.CustPONumber:str = obj["CustPONumber"]
      """  Used by the freight web service  """  
      self.DropShip:bool = obj["DropShip"]
      """  Used by the freight web service  """  
      self.FFCity:str = obj["FFCity"]
      """  Used by the freight web service  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Used by the freight web service  """  
      self.FFContact:str = obj["FFContact"]
      """  Used by the freight web service  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Used by the freight web service  """  
      self.FFID:str = obj["FFID"]
      """  Used by the freight web service  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Used by the freight web service  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  Used by the freight web service  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Used by the freight web service  """  
      self.FFState:str = obj["FFState"]
      """  Used by the freight web service  """  
      self.FFZip:str = obj["FFZip"]
      """  Used by the freight web service  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Used by the freight web service  """  
      self.JobNumber:str = obj["JobNumber"]
      """  Used by the freight web service  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Used by the freight web service  """  
      self.OrderNum:str = obj["OrderNum"]
      """  Used by the freight web service  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Used by the freight web service  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Used by the freight web service  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Used by the freight web service  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Used by the freight web service  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Used by the freight web service  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Used by the freight web service  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Used by the freight web service  """  
      self.PayFlag:bool = obj["PayFlag"]
      """  Used by the freight web service  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Used by the freight web service  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Used by the freight web service  """  
      self.TotalOrderValueCurrencyUOM:str = obj["TotalOrderValueCurrencyUOM"]
      self.ShipmentTypeDesc:str = obj["ShipmentTypeDesc"]
      """  Readable translated description of ShipmentType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Inter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  This field is reserved for future development.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.BillToAddrList:str = obj["BillToAddrList"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates of TranDocTypeID is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the option to void the legal number is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Logical indicating to the UI that the weight prompt is to be enabled.  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration is setup for master pack  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height field is enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length field is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width field is enabled.  """  
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      self.AddrList:str = obj["AddrList"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if information on the master pack can be modified after the document has been printed.  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sumo of the value of the items in the carton  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  carton Length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if the option to assign a legal number is available.  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      """  Formatted address column for ShipTo field  """  
      self.SoldToAddrFormatted:str = obj["SoldToAddrFormatted"]
      """  Formatted address column for Sold To  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterPackTableset:
   def __init__(self, obj):
      self.MasterPack:list[Erp_Tablesets_MasterPackRow] = obj["MasterPack"]
      self.MasterPackAttch:list[Erp_Tablesets_MasterPackAttchRow] = obj["MasterPackAttch"]
      self.MasterPackDtl:list[Erp_Tablesets_MasterPackDtlRow] = obj["MasterPackDtl"]
      self.MasterPackUPS:list[Erp_Tablesets_MasterPackUPSRow] = obj["MasterPackUPS"]
      self.CartonDetail:list[Erp_Tablesets_CartonDetailRow] = obj["CartonDetail"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MasterPackUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantity View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email adress to be used for notifications.  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the UPS Quantum View is to be enabled.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterpackListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Voided:bool = obj["Voided"]
      """  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.ICReceived:bool = obj["ICReceived"]
      """  Inter Company Received flag  """  
      self.XRefPackNum:str = obj["XRefPackNum"]
      """  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Populated from OrderHed.BTCustNum.  """  
      self.BTConNum:int = obj["BTConNum"]
      """  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  This field is reserved for future development.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton height  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.CartonLength:int = obj["CartonLength"]
      """  carton Length  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sumo of the value of the items in the carton  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage Number.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height field is enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length field is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width field is enabled.  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Logical indicating to the UI that the weight prompt is to be enabled.  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if the option to assign a legal number is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the option to void the legal number is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration is setup for master pack  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if information on the master pack can be modified after the document has been printed.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates of TranDocTypeID is available for input  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.OurBankBankName:str = obj["OurBankBankName"]
      """  The Bank's full name.  """  
      self.OurBankDescription:str = obj["OurBankDescription"]
      """  Full description of the bank account.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasterpackListTableset:
   def __init__(self, obj):
      self.MasterpackList:list[Erp_Tablesets_MasterpackListRow] = obj["MasterpackList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMasterPackTableset:
   def __init__(self, obj):
      self.MasterPack:list[Erp_Tablesets_MasterPackRow] = obj["MasterPack"]
      self.MasterPackAttch:list[Erp_Tablesets_MasterPackAttchRow] = obj["MasterPackAttch"]
      self.MasterPackDtl:list[Erp_Tablesets_MasterPackDtlRow] = obj["MasterPackDtl"]
      self.MasterPackUPS:list[Erp_Tablesets_MasterPackUPSRow] = obj["MasterPackUPS"]
      self.CartonDetail:list[Erp_Tablesets_CartonDetailRow] = obj["CartonDetail"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateDigitalSignature_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GenerateDigitalSignature_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCustPayBTFlagDefaults_input:
   """ Required : 
   ipPayFlag
   """  
   def __init__(self, obj):
      self.ipPayFlag:str = obj["ipPayFlag"]
      pass

class GetCustPayBTFlagDefaults_output:
   def __init__(self, obj):
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class GetListEnhanced_input:
   """ Required : 
   ipType
   ipStatus
   ipSortBy
   ipStartAtPackNum
   ipStartAtShipDate
   ipStartAtLegalNumber
   ipShipViaCode
   ipCustNum
   ipShipToNum
   ipVendorNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      self.ipStatus:str = obj["ipStatus"]
      self.ipSortBy:str = obj["ipSortBy"]
      self.ipStartAtPackNum:int = obj["ipStartAtPackNum"]
      self.ipStartAtShipDate:str = obj["ipStartAtShipDate"]
      self.ipStartAtLegalNumber:str = obj["ipStartAtLegalNumber"]
      self.ipShipViaCode:str = obj["ipShipViaCode"]
      self.ipCustNum:int = obj["ipCustNum"]
      self.ipShipToNum:str = obj["ipShipToNum"]
      self.ipVendorNum:int = obj["ipVendorNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListEnhanced_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterpackListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_MasterpackListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMiscPayBTFlagDefaults_input:
   """ Required : 
   ipPayFlag
   """  
   def __init__(self, obj):
      self.ipPayFlag:str = obj["ipPayFlag"]
      pass

class GetMiscPayBTFlagDefaults_output:
   def __init__(self, obj):
      pass

class GetNewMasterPackAttch_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewMasterPackAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMasterPackDtl_input:
   """ Required : 
   ds
   mpackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.mpackLine:int = obj["mpackLine"]
      pass

class GetNewMasterPackDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMasterPackUPS_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewMasterPackUPS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMasterPack_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GetNewMasterPack_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackClass_input:
   """ Required : 
   ipPkgClass
   ds
   """  
   def __init__(self, obj):
      self.ipPkgClass:str = obj["ipPkgClass"]
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GetPackClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackaging_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GetPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPayBTFlagDefaults_input:
   """ Required : 
   ipPayFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPayFlag:str = obj["ipPayFlag"]
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GetPayBTFlagDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMasterPack
   whereClauseMasterPackAttch
   whereClauseMasterPackDtl
   whereClauseMasterPackUPS
   whereClauseCartonDetail
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMasterPack:str = obj["whereClauseMasterPack"]
      self.whereClauseMasterPackAttch:str = obj["whereClauseMasterPackAttch"]
      self.whereClauseMasterPackDtl:str = obj["whereClauseMasterPackDtl"]
      self.whereClauseMasterPackUPS:str = obj["whereClauseMasterPackUPS"]
      self.whereClauseCartonDetail:str = obj["whereClauseCartonDetail"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetScale_input:
   """ Required : 
   workstationID
   """  
   def __init__(self, obj):
      self.workstationID:str = obj["workstationID"]
      pass

class GetScale_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ScaleID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetShipDetails_input:
   """ Required : 
   ds
   PackNum
   DtlPackNum
   ShipmentType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      self.PackNum:int = obj["PackNum"]
      """  Master Pack ID  """  
      self.DtlPackNum:int = obj["DtlPackNum"]
      """  Detail Pack ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Shipment type:Sales,Misc,Sub or Transfer  """  
      pass

class GetShipDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSubPayBTFlagDefaults_input:
   """ Required : 
   ipPayFlag
   """  
   def __init__(self, obj):
      self.ipPayFlag:str = obj["ipPayFlag"]
      pass

class GetSubPayBTFlagDefaults_output:
   def __init__(self, obj):
      pass

class GetTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class GetTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTransferPayBTFlagDefaults_input:
   """ Required : 
   ipPayFlag
   """  
   def __init__(self, obj):
      self.ipPayFlag:str = obj["ipPayFlag"]
      pass

class GetTransferPayBTFlagDefaults_output:
   def __init__(self, obj):
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

class OpenCarton_input:
   """ Required : 
   iPackNum
   ipResetCODCharges
   ipResetInsCharges
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to open  """  
      self.ipResetCODCharges:bool = obj["ipResetCODCharges"]
      """  Indicates if the CODAmount is to be reset to zero  """  
      self.ipResetInsCharges:bool = obj["ipResetInsCharges"]
      """  Indicates if the DeclaredAmt is to be reset to zero  """  
      pass

class OpenCarton_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessFreightInfo_input:
   """ Required : 
   iPackNum
   ds
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      self.ds:list[Erp_Tablesets_FreightInfoResponseTableset] = obj["ds"]
      pass

class ProcessFreightInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FreightInfoResponseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessUnFreightInfo_input:
   """ Required : 
   iPackNum
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      pass

class ProcessUnFreightInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetUPSQVEnable_input:
   """ Required : 
   ipQVEnable
   ds
   """  
   def __init__(self, obj):
      self.ipQVEnable:bool = obj["ipQVEnable"]
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class SetUPSQVEnable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetUPSQVShipStatus_input:
   """ Required : 
   ipShipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipShipStatus:str = obj["ipShipStatus"]
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class SetUPSQVShipStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StageCarton_input:
   """ Required : 
   iPackNum
   ds
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to Stage  """  
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class StageCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMasterPackTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMasterPackTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateManifestChargeAmts_input:
   """ Required : 
   ipAmountType
   ipAction
   ds
   """  
   def __init__(self, obj):
      self.ipAmountType:str = obj["ipAmountType"]
      self.ipAction:bool = obj["ipAction"]
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class UpdateManifestChargeAmts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MasterPackTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidCarton_input:
   """ Required : 
   iPackNum
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to void  """  
      pass

class VoidCarton_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

class VoidLegalNumber_input:
   """ Required : 
   ipPackNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MasterPackTableset] = obj["returnObj"]
      pass

