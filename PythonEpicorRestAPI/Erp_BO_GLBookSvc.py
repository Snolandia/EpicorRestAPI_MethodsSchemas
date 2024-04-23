import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLBookSvc
# Description: GL Book Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBooks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBooks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks",headers=creds) as resp:
           return await resp.json()

async def post_GLBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBookRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBookRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID(Company, BookID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBook item
   Description: Calls GetByID to retrieve the GLBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBooks_Company_BookID(Company, BookID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBook for the service
   Description: Calls UpdateExt to update GLBook. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBookRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBooks_Company_BookID(Company, BookID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBook item
   Description: Call UpdateExt to delete GLBook item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_GLAccountMasks(Company, BookID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLAccountMasks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLAccountMasks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountMasksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/GLAccountMasks",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_GLAccountMasks_Company_COACode_BookID_MaskType_GLMaskedAccount(Company, BookID, COACode, MaskType, GLMaskedAccount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAccountMask item
   Description: Calls GetByID to retrieve the GLAccountMask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccountMask1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param MaskType: Desc: MaskType   Required: True   Allow empty value : True
      :param GLMaskedAccount: Desc: GLMaskedAccount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/GLAccountMasks(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_BVRules(Company, BookID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BVRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BVRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BVRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/BVRules",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_BVRules_Company_BVRuleUID(Company, BookID, BVRuleUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BVRule item
   Description: Calls GetByID to retrieve the BVRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BVRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param BVRuleUID: Desc: BVRuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BVRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/BVRules(" + Company + "," + BVRuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_GLBookPackageSegmentMaps(Company, BookID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLBookPackageSegmentMaps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBookPackageSegmentMaps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookPackageSegmentMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/GLBookPackageSegmentMaps",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_GLBookPackageSegmentMaps_Company_BookID_Package_SourceSegmentNbr(Company, BookID, Package, SourceSegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBookPackageSegmentMap item
   Description: Calls GetByID to retrieve the GLBookPackageSegmentMap item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBookPackageSegmentMap1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param Package: Desc: Package   Required: True   Allow empty value : True
      :param SourceSegmentNbr: Desc: SourceSegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookPackageSegmentMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/GLBookPackageSegmentMaps(" + Company + "," + BookID + "," + Package + "," + SourceSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_GLBookAttches(Company, BookID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLBookAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBookAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/GLBookAttches",headers=creds) as resp:
           return await resp.json()

async def get_GLBooks_Company_BookID_GLBookAttches_Company_BookID_DrawingSeq(Company, BookID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBookAttch item
   Description: Calls GetByID to retrieve the GLBookAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBookAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBooks(" + Company + "," + BookID + ")/GLBookAttches(" + Company + "," + BookID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAccountMasks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAccountMasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccountMasks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccountMasksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLAccountMasks",headers=creds) as resp:
           return await resp.json()

async def post_GLAccountMasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccountMasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLAccountMasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAccountMasks_Company_COACode_BookID_MaskType_GLMaskedAccount(Company, COACode, BookID, MaskType, GLMaskedAccount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAccountMask item
   Description: Calls GetByID to retrieve the GLAccountMask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccountMask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param MaskType: Desc: MaskType   Required: True   Allow empty value : True
      :param GLMaskedAccount: Desc: GLMaskedAccount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLAccountMasks(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAccountMasks_Company_COACode_BookID_MaskType_GLMaskedAccount(Company, COACode, BookID, MaskType, GLMaskedAccount, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAccountMask for the service
   Description: Calls UpdateExt to update GLAccountMask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccountMask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param MaskType: Desc: MaskType   Required: True   Allow empty value : True
      :param GLMaskedAccount: Desc: GLMaskedAccount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAccountMasksRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLAccountMasks(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAccountMasks_Company_COACode_BookID_MaskType_GLMaskedAccount(Company, COACode, BookID, MaskType, GLMaskedAccount, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAccountMask item
   Description: Call UpdateExt to delete GLAccountMask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccountMask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param MaskType: Desc: MaskType   Required: True   Allow empty value : True
      :param GLMaskedAccount: Desc: GLMaskedAccount   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLAccountMasks(" + Company + "," + COACode + "," + BookID + "," + MaskType + "," + GLMaskedAccount + ")",headers=creds) as resp:
           return await resp.json()

async def get_BVRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BVRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BVRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BVRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/BVRules",headers=creds) as resp:
           return await resp.json()

async def post_BVRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BVRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BVRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BVRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/BVRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BVRules_Company_BVRuleUID(Company, BVRuleUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BVRule item
   Description: Calls GetByID to retrieve the BVRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BVRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BVRuleUID: Desc: BVRuleUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BVRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/BVRules(" + Company + "," + BVRuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BVRules_Company_BVRuleUID(Company, BVRuleUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BVRule for the service
   Description: Calls UpdateExt to update BVRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BVRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BVRuleUID: Desc: BVRuleUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BVRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/BVRules(" + Company + "," + BVRuleUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BVRules_Company_BVRuleUID(Company, BVRuleUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BVRule item
   Description: Call UpdateExt to delete BVRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BVRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BVRuleUID: Desc: BVRuleUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/BVRules(" + Company + "," + BVRuleUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBookPackageSegmentMaps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBookPackageSegmentMaps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBookPackageSegmentMaps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookPackageSegmentMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookPackageSegmentMaps",headers=creds) as resp:
           return await resp.json()

async def post_GLBookPackageSegmentMaps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBookPackageSegmentMaps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBookPackageSegmentMapRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBookPackageSegmentMapRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookPackageSegmentMaps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBookPackageSegmentMaps_Company_BookID_Package_SourceSegmentNbr(Company, BookID, Package, SourceSegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBookPackageSegmentMap item
   Description: Calls GetByID to retrieve the GLBookPackageSegmentMap item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBookPackageSegmentMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param Package: Desc: Package   Required: True   Allow empty value : True
      :param SourceSegmentNbr: Desc: SourceSegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookPackageSegmentMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookPackageSegmentMaps(" + Company + "," + BookID + "," + Package + "," + SourceSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBookPackageSegmentMaps_Company_BookID_Package_SourceSegmentNbr(Company, BookID, Package, SourceSegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBookPackageSegmentMap for the service
   Description: Calls UpdateExt to update GLBookPackageSegmentMap. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBookPackageSegmentMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param Package: Desc: Package   Required: True   Allow empty value : True
      :param SourceSegmentNbr: Desc: SourceSegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBookPackageSegmentMapRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookPackageSegmentMaps(" + Company + "," + BookID + "," + Package + "," + SourceSegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBookPackageSegmentMaps_Company_BookID_Package_SourceSegmentNbr(Company, BookID, Package, SourceSegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBookPackageSegmentMap item
   Description: Call UpdateExt to delete GLBookPackageSegmentMap item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBookPackageSegmentMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param Package: Desc: Package   Required: True   Allow empty value : True
      :param SourceSegmentNbr: Desc: SourceSegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookPackageSegmentMaps(" + Company + "," + BookID + "," + Package + "," + SourceSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBookAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBookAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBookAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookAttches",headers=creds) as resp:
           return await resp.json()

async def post_GLBookAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBookAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBookAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBookAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBookAttches_Company_BookID_DrawingSeq(Company, BookID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBookAttch item
   Description: Calls GetByID to retrieve the GLBookAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBookAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBookAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookAttches(" + Company + "," + BookID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBookAttches_Company_BookID_DrawingSeq(Company, BookID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBookAttch for the service
   Description: Calls UpdateExt to update GLBookAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBookAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBookAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookAttches(" + Company + "," + BookID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBookAttches_Company_BookID_DrawingSeq(Company, BookID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBookAttch item
   Description: Call UpdateExt to delete GLBookAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBookAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/GLBookAttches(" + Company + "," + BookID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegmentNameLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegmentNameLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegmentNameLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentNameListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/COASegmentNameLists",headers=creds) as resp:
           return await resp.json()

async def post_COASegmentNameLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegmentNameLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegmentNameListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegmentNameListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/COASegmentNameLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegmentNameLists_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegmentNameList item
   Description: Calls GetByID to retrieve the COASegmentNameList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegmentNameList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentNameListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/COASegmentNameLists(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegmentNameLists_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegmentNameList for the service
   Description: Calls UpdateExt to update COASegmentNameList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegmentNameList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegmentNameListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/COASegmentNameLists(" + Company + "," + COACode + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegmentNameLists_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegmentNameList item
   Description: Call UpdateExt to delete COASegmentNameList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegmentNameList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/COASegmentNameLists(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_MapBooks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MapBooks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MapBooks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MapBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks",headers=creds) as resp:
           return await resp.json()

async def post_MapBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MapBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MapBookRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MapBookRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MapBooks_Company_LinkID_TrgBook(Company, LinkID, TrgBook, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MapBook item
   Description: Calls GetByID to retrieve the MapBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MapBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MapBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks(" + Company + "," + LinkID + "," + TrgBook + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MapBooks_Company_LinkID_TrgBook(Company, LinkID, TrgBook, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MapBook for the service
   Description: Calls UpdateExt to update MapBook. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MapBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MapBookRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks(" + Company + "," + LinkID + "," + TrgBook + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MapBooks_Company_LinkID_TrgBook(Company, LinkID, TrgBook, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MapBook item
   Description: Call UpdateExt to delete MapBook item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MapBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks(" + Company + "," + LinkID + "," + TrgBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_MapBooks_Company_LinkID_TrgBook_MapACTTypes(Company, LinkID, TrgBook, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MapACTTypes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MapACTTypes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MapACTTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks(" + Company + "," + LinkID + "," + TrgBook + ")/MapACTTypes",headers=creds) as resp:
           return await resp.json()

async def get_MapBooks_Company_LinkID_TrgBook_MapACTTypes_Company_LinkID_ACTTypeUID_TrgBook(Company, LinkID, TrgBook, ACTTypeUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MapACTType item
   Description: Calls GetByID to retrieve the MapACTType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MapACTType1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MapACTTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapBooks(" + Company + "," + LinkID + "," + TrgBook + ")/MapACTTypes(" + Company + "," + LinkID + "," + ACTTypeUID + "," + TrgBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_MapACTTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MapACTTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MapACTTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MapACTTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapACTTypes",headers=creds) as resp:
           return await resp.json()

async def post_MapACTTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MapACTTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MapACTTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MapACTTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapACTTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MapACTTypes_Company_LinkID_ACTTypeUID_TrgBook(Company, LinkID, ACTTypeUID, TrgBook, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MapACTType item
   Description: Calls GetByID to retrieve the MapACTType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MapACTType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MapACTTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapACTTypes(" + Company + "," + LinkID + "," + ACTTypeUID + "," + TrgBook + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MapACTTypes_Company_LinkID_ACTTypeUID_TrgBook(Company, LinkID, ACTTypeUID, TrgBook, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MapACTType for the service
   Description: Calls UpdateExt to update MapACTType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MapACTType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MapACTTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapACTTypes(" + Company + "," + LinkID + "," + ACTTypeUID + "," + TrgBook + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MapACTTypes_Company_LinkID_ACTTypeUID_TrgBook(Company, LinkID, ACTTypeUID, TrgBook, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MapACTType item
   Description: Call UpdateExt to delete MapACTType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MapACTType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LinkID: Desc: LinkID   Required: True
      :param ACTTypeUID: Desc: ACTTypeUID   Required: True
      :param TrgBook: Desc: TrgBook   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/MapACTTypes(" + Company + "," + LinkID + "," + ACTTypeUID + "," + TrgBook + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBookListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBook, whereClauseGLBookAttch, whereClauseGLAccountMasks, whereClauseBVRule, whereClauseCOASegmentNameList, whereClauseMapBook, whereClauseMapACTType, whereClauseGLBookPackageSegmentMap, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLBook=" + whereClauseGLBook
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBookAttch=" + whereClauseGLBookAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLAccountMasks=" + whereClauseGLAccountMasks
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBVRule=" + whereClauseBVRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOASegmentNameList=" + whereClauseCOASegmentNameList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMapBook=" + whereClauseMapBook
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMapACTType=" + whereClauseMapACTType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBookPackageSegmentMap=" + whereClauseGLBookPackageSegmentMap
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bookID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "bookID=" + bookID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBookType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBookType
   Description: Check  value
   OperationID: CheckBookType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBookType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBookType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckMainBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckMainBook
   Description: Check PartNum value
   OperationID: CheckMainBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckMainBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMainBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillACTTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillACTTypes
   Description: Create new MapBook.
   OperationID: FillACTTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillACTTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillACTTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLink
   Description: Create new MapBook.
   OperationID: GetNewLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCurrencyCode
   Description: Check to see if Currency can be changed
   OperationID: OnChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAccountDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAccountDescription
   Description: Get Account Description
   OperationID: GetAccountDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAccountDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccountDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateStdAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateStdAccount
   OperationID: ValidateStdAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateStdAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStdAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteChgLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteChgLog
   Description: Write change log then book mapping is doing something with GL transaction types..
   OperationID: WriteChgLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteChgLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteChgLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListManual(epicorHeaders = None):
   """  
   Summary: Invoke method GetListManual
   Description: Returns list of GLBooks with 'Journal' open balance update option
   OperationID: GetListManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckDataInGLJrnDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDataInGLJrnDtl
   Description: Determing existance of GL transactions for given Book ID
   OperationID: CheckDataInGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDataInGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDataInGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckVerifyBalanceFlag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckVerifyBalanceFlag
   Description: Returns current verify balance flag
   OperationID: CheckVerifyBalanceFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckVerifyBalanceFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVerifyBalanceFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDataInActiveRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDataInActiveRevision
   Description: Check if the Book is configured to receive GL transactions in active revision of some GL Transaction Types.
   OperationID: CheckDataInActiveRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDataInActiveRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDataInActiveRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BookExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BookExists
   Description: Check if the Book exists in the system.
   OperationID: BookExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BookExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BookExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidAccount
   OperationID: ValidAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevalueOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevalueOpt
   Description: On Revalue Option changing
   OperationID: ChangeRevalueOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevalueOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalueOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateType
   Description: On Rate Type changing
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAccountContext(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAccountContext
   Description: On Account context changing
   OperationID: ChangeAccountContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAccountContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAccountContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveACTTypesToReview(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveACTTypesToReview
   Description: List of ACTTypes to review after segment map has changed.
   OperationID: RetrieveACTTypesToReview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveACTTypesToReview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveACTTypesToReview_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MultiCurrencyChecksLicensed(epicorHeaders = None):
   """  
   Summary: Invoke method MultiCurrencyChecksLicensed
   Description: Check if any License for MultiCurrencyManagement module. Developed for Kinetic.
   OperationID: MultiCurrencyChecksLicensed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MultiCurrencyChecksLicensed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewLinkWithID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLinkWithID
   Description: Get New Link to Source Book - with link ID.
   OperationID: GetNewLinkWithID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLinkWithID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLinkWithID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGLAccount
   Description: Check COA segments in GL Accounts.
   OperationID: CheckGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMainBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMainBook
   Description: Change Main Book
   OperationID: ChangeMainBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMainBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMainBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidGLAccount
   Description: Validate GL Account
   OperationID: ValidGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsBalanceSegmentUpdated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsBalanceSegmentUpdated
   Description: Check if BalanceSegment Updated.
   OperationID: IsBalanceSegmentUpdated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsBalanceSegmentUpdated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsBalanceSegmentUpdated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSrcBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSrcBook
   Description: Check entering Source Book.
   OperationID: CheckSrcBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSrcBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSrcBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillDataForSrcBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillDataForSrcBook
   Description: Set Datafor a new Source Book, including filling the list of transactions and COA codes for target/source books.
   OperationID: FillDataForSrcBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillDataForSrcBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillDataForSrcBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMappingStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMappingStatus
   Description: Disable or enable mappings.
   OperationID: ChangeMappingStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMappingStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMappingStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateTransactionTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateTransactionTypes
   Description: Update Transaction Types.
   OperationID: UpdateTransactionTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateTransactionTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTransactionTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MaskValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MaskValidate
   Description: Test if account masks are valid
   OperationID: MaskValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MaskValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MaskValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBook
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBookAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBookAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBookAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBookAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBookAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAccountMasks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAccountMasks
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAccountMasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAccountMasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAccountMasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBVRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBVRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBVRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBVRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBVRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegmentNameList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegmentNameList
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegmentNameList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegmentNameList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegmentNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMapBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMapBook
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMapBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMapBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMapBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBookPackageSegmentMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBookPackageSegmentMap
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBookPackageSegmentMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBookPackageSegmentMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBookPackageSegmentMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BVRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BVRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentNameListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegmentNameListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccountMasksRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAccountMasksRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookPackageSegmentMapRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookPackageSegmentMapRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBookRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBookRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MapACTTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MapACTTypeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MapBookRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MapBookRow] = obj["value"]
      pass

class Erp_Tablesets_BVRuleRow:
   def __init__(self, obj):
      self.BVRuleUID:int = obj["BVRuleUID"]
      """  Unique value.Primary key  """  
      self.VRuleUID:int = obj["VRuleUID"]
      """  Technical key of Validation Rule  """  
      self.Description:str = obj["Description"]
      """  Validation rule description  """  
      self.Action:str = obj["Action"]
      """  Error, Ignor, Warning, Autocorrect, Autocorrect with warning  """  
      self.VLevel:str = obj["VLevel"]
      """  Validation level : Book, Booking Rule, Company etc  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to Book.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default validation rules for ABT templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ActionList:str = obj["ActionList"]
      """  List of actions (used in combo boxes).  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentNameListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountMasksRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.BookID:str = obj["BookID"]
      """  GL Book ID  """  
      self.MaskType:str = obj["MaskType"]
      """   Indicates the type of Mask to search and apply.  Valid values include:
DB = Daily Balance
RU = Roll-Up Accounts
RT = Reference Type  """  
      self.GLMaskedAccount:str = obj["GLMaskedAccount"]
      """  GL Account Mask in COA segment number format separated by the vertical bar.  This field is not intended ofr end user use.  """  
      self.GLMaskAcctDisp:str = obj["GLMaskAcctDisp"]
      """  GL Account Mask in COA display order format  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.TgtAccount:str = obj["TgtAccount"]
      """  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks.  This field is intended for internal use only.  """  
      self.TgtAcctDisp:str = obj["TgtAcctDisp"]
      """  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks  """  
      self.TgtSegValue1:str = obj["TgtSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.TgtSegValue2:str = obj["TgtSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.TgtSegValue3:str = obj["TgtSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.TgtSegValue4:str = obj["TgtSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.TgtSegValue5:str = obj["TgtSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.TgtSegValue6:str = obj["TgtSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.TgtSegValue7:str = obj["TgtSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.TgtSegValue8:str = obj["TgtSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.TgtSegValue9:str = obj["TgtSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.TgtSegValue10:str = obj["TgtSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.TgtSegValue11:str = obj["TgtSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.TgtSegValue12:str = obj["TgtSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.TgtSegValue13:str = obj["TgtSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.TgtSegValue14:str = obj["TgtSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.TgtSegValue15:str = obj["TgtSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.TgtSegValue16:str = obj["TgtSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.TgtSegValue17:str = obj["TgtSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.TgtSegValue18:str = obj["TgtSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.TgtSegValue19:str = obj["TgtSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.TgtSegValue20:str = obj["TgtSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.MaskRank:int = obj["MaskRank"]
      """  Order in which Mask is applied  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
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

class Erp_Tablesets_GLBookListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.COACodeDescription:str = obj["COACodeDescription"]
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenBalUpdateOpt:str = obj["OpenBalUpdateOpt"]
      """  Indicates how opening balances will be updated  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookPackageSegmentMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.Package:str = obj["Package"]
      """  Posting Rules Package  """  
      self.SourceSegmentNbr:int = obj["SourceSegmentNbr"]
      """  Segment Number in Posting Rules Package  """  
      self.TargetSegmentNbr:int = obj["TargetSegmentNbr"]
      """  Segment Number in COA of the Book  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date/ time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.TargetSegmentName:str = obj["TargetSegmentName"]
      """  Target Segment Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourceSegmentName:str = obj["SourceSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.COABalFmtChg:bool = obj["COABalFmtChg"]
      """  Indiates if the blaance account structure has changed on the COA.  Yes indicates it has changed and the balance rebuild utility needs to run.  This field is used internally and is not intended for end-user use.  """  
      self.REAccount:str = obj["REAccount"]
      """  Retained Earnings Account.  May be actual account or a mask  """  
      self.RESegValue1:str = obj["RESegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.RESegValue2:str = obj["RESegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.RESegValue3:str = obj["RESegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.RESegValue4:str = obj["RESegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.RESegValue5:str = obj["RESegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.RESegValue6:str = obj["RESegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.RESegValue7:str = obj["RESegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.RESegValue8:str = obj["RESegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.RESegValue9:str = obj["RESegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.RESegValue10:str = obj["RESegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.RESegValue11:str = obj["RESegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.RESegValue12:str = obj["RESegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.RESegValue13:str = obj["RESegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.RESegValue14:str = obj["RESegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.RESegValue15:str = obj["RESegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.RESegValue16:str = obj["RESegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.RESegValue17:str = obj["RESegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.RESegValue18:str = obj["RESegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.RESegValue19:str = obj["RESegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.RESegValue20:str = obj["RESegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RndTolerance:int = obj["RndTolerance"]
      """  RoundTolerance  """  
      self.RndAccount:str = obj["RndAccount"]
      """  The Account is used  in case auto balancing with rounding difference.  """  
      self.RndSegValue1:str = obj["RndSegValue1"]
      """  SegValue1 of Round Account  """  
      self.RndSegValue2:str = obj["RndSegValue2"]
      """  SegValue2 -  of Round Account  """  
      self.RndSegValue3:str = obj["RndSegValue3"]
      """  SegValue3 of RoundAccount  """  
      self.RndSegValue4:str = obj["RndSegValue4"]
      """  SegValue4 of RoundAccount  """  
      self.RndSegValue5:str = obj["RndSegValue5"]
      """  SegValue5 of RoundAccount  """  
      self.RndSegValue6:str = obj["RndSegValue6"]
      """  SegValue6 of Round Account  """  
      self.RndSegValue7:str = obj["RndSegValue7"]
      """  SegValue7 of RoundAccount  """  
      self.RndSegValue8:str = obj["RndSegValue8"]
      """  SegValue8 - of RoundAccount  """  
      self.RndSegValue9:str = obj["RndSegValue9"]
      """  SegValue9 - RoundAccount  """  
      self.RndSegValue10:str = obj["RndSegValue10"]
      """  SegValue10 - of RoundAccount  """  
      self.RndSegValue11:str = obj["RndSegValue11"]
      """  SegValue11 fo RoundAccount  """  
      self.RndSegValue12:str = obj["RndSegValue12"]
      """  SegValue12 of RoundAccount  """  
      self.RndSegValue13:str = obj["RndSegValue13"]
      """  SegValue13 of RoundAccount  """  
      self.RndSegValue14:str = obj["RndSegValue14"]
      """  SegValue14 of RoundAccount  """  
      self.RndSegValue15:str = obj["RndSegValue15"]
      """  SegValue15 of RoundAccount  """  
      self.RndSegValue16:str = obj["RndSegValue16"]
      """  SegValue16 of RoundAccount  """  
      self.RndSegValue17:str = obj["RndSegValue17"]
      """  SegValue17 of RoundAccount  """  
      self.RndSegValue18:str = obj["RndSegValue18"]
      """  SegValue18 of RoundAccount  """  
      self.RndSegValue19:str = obj["RndSegValue19"]
      """  SegValue19 of RoundAccount  """  
      self.RndSegValue20:str = obj["RndSegValue20"]
      """  SegValue20 of RoundAccount  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the book.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenBalUpdateOpt:str = obj["OpenBalUpdateOpt"]
      """  Indicates how opening balances will be updated  """  
      self.FromNatAccount:str = obj["FromNatAccount"]
      """  Report Default Natural Account From  """  
      self.ToNatAccount:str = obj["ToNatAccount"]
      """  Report Default Natural Account To  """  
      self.LevelList:str = obj["LevelList"]
      """  Report Default LevelList  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  DebitRateType  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  CreditRateType  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  GainAcctDesc  """  
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  LossAcctDesc  """  
      self.DefaultPackage:str = obj["DefaultPackage"]
      """  Posting Rules Package that is used by “Import GL Transaction Types” conversion program to load posting rules when there is no Revision for the GL Transaction Type being updated. Available only for Main Book.  """  
      self.EnableBookType:bool = obj["EnableBookType"]
      self.EnableCalendar:bool = obj["EnableCalendar"]
      """  Flag to indicate if the calendar id is available for input.  """  
      self.EnableCurrency:bool = obj["EnableCurrency"]
      """  Flag to indicate if the currency is available for input.  """  
      self.FiscalCalendarDesc:str = obj["FiscalCalendarDesc"]
      """  Fiscal Calendar Description  """  
      self.GLControlType:str = obj["GLControlType"]
      self.isDefaultBook:bool = obj["isDefaultBook"]
      """  The user uses this field to define the Book as Default (Main).  """  
      self.MainBookID:str = obj["MainBookID"]
      """  The BookID of the GL Book which is flagged as 'Main'.  """  
      self.REAccountDesc:str = obj["REAccountDesc"]
      """  RE Account DEscription.  """  
      self.RevalueOptDesc:str = obj["RevalueOptDesc"]
      self.RndAccoundDesc:str = obj["RndAccoundDesc"]
      self.SegmentMapIsNotRequired:bool = obj["SegmentMapIsNotRequired"]
      self.BitFlag:int = obj["BitFlag"]
      self.COACodePerBalFmt:str = obj["COACodePerBalFmt"]
      self.COACodeDescription:str = obj["COACodeDescription"]
      self.CreditRateTypeDescription:str = obj["CreditRateTypeDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DebitRateTypeDescription:str = obj["DebitRateTypeDescription"]
      self.DefaultPackagePackageName:str = obj["DefaultPackagePackageName"]
      self.RndAccountGLShortAcct:str = obj["RndAccountGLShortAcct"]
      self.RndAccountGLAcctDisp:str = obj["RndAccountGLAcctDisp"]
      self.RndAccountAccountDesc:str = obj["RndAccountAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MapACTTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LinkID:int = obj["LinkID"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      self.DisplayName:str = obj["DisplayName"]
      self.RevisionCode:str = obj["RevisionCode"]
      self.RevisionStatus:str = obj["RevisionStatus"]
      self.Limited:bool = obj["Limited"]
      self.EnableMapping:bool = obj["EnableMapping"]
      self.MapExists:bool = obj["MapExists"]
      self.TrgBook:str = obj["TrgBook"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MapBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LinkID:int = obj["LinkID"]
      """  LinkID  """  
      self.TrgBook:str = obj["TrgBook"]
      """  TrgBook  """  
      self.SrcBook:str = obj["SrcBook"]
      """  SrcBook  """  
      self.TranCurr:int = obj["TranCurr"]
      """  TranCurr  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  COAMapUID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SrcBookCOA:str = obj["SrcBookCOA"]
      """  Source Book COA  """  
      self.TrgBookCOA:str = obj["TrgBookCOA"]
      """  Target Book COA  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BookExists_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      pass

class BookExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ChangeAccountContext_input:
   """ Required : 
   context
   """  
   def __init__(self, obj):
      self.context:str = obj["context"]
      pass

class ChangeAccountContext_output:
   def __init__(self, obj):
      pass

class ChangeMainBook_input:
   """ Required : 
   newMainBookID
   oldMainBook
   """  
   def __init__(self, obj):
      self.newMainBookID:str = obj["newMainBookID"]
      self.oldMainBook:str = obj["oldMainBook"]
      pass

class ChangeMainBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.currentIsDefaultBook:bool = obj["currentIsDefaultBook"]
      pass

      """  output parameters  """  

class ChangeMappingStatus_input:
   """ Required : 
   ifEnable
   linkID
   trgBook
   ds
   """  
   def __init__(self, obj):
      self.ifEnable:bool = obj["ifEnable"]
      self.linkID:int = obj["linkID"]
      self.trgBook:str = obj["trgBook"]
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class ChangeMappingStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRateType_input:
   """ Required : 
   rateType
   isCredit
   """  
   def __init__(self, obj):
      self.rateType:str = obj["rateType"]
      self.isCredit:bool = obj["isCredit"]
      pass

class ChangeRateType_output:
   def __init__(self, obj):
      pass

class ChangeRevalueOpt_input:
   """ Required : 
   revalueOption
   """  
   def __init__(self, obj):
      self.revalueOption:str = obj["revalueOption"]
      pass

class ChangeRevalueOpt_output:
   def __init__(self, obj):
      pass

class CheckBookType_input:
   """ Required : 
   ipBookType
   ipMainBook
   """  
   def __init__(self, obj):
      self.ipBookType:int = obj["ipBookType"]
      """  The proposed Book  """  
      self.ipMainBook:bool = obj["ipMainBook"]
      """  The flag for Main Book  """  
      pass

class CheckBookType_output:
   def __init__(self, obj):
      pass

class CheckDataInActiveRevision_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      pass

class CheckDataInActiveRevision_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckDataInGLJrnDtl_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  Book ID  """  
      pass

class CheckDataInGLJrnDtl_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckGLAccount_input:
   """ Required : 
   ipTypeOfAccount
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipTypeOfAccount:str = obj["ipTypeOfAccount"]
      self.ipGLAccount:str = obj["ipGLAccount"]
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class CheckGLAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckMainBook_input:
   """ Required : 
   ipBookType
   ipMainBook
   """  
   def __init__(self, obj):
      self.ipBookType:int = obj["ipBookType"]
      """  The Book Type  """  
      self.ipMainBook:bool = obj["ipMainBook"]
      """  The proposed flag for Main Book  """  
      pass

class CheckMainBook_output:
   def __init__(self, obj):
      pass

class CheckSrcBook_input:
   """ Required : 
   ipProposedSrcBook
   ipTrgBook
   """  
   def __init__(self, obj):
      self.ipProposedSrcBook:str = obj["ipProposedSrcBook"]
      self.ipTrgBook:str = obj["ipTrgBook"]
      pass

class CheckSrcBook_output:
   def __init__(self, obj):
      pass

class CheckVerifyBalanceFlag_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      pass

class CheckVerifyBalanceFlag_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DefaultsOnAdd_input:
   """ Required : 
   ipTypeOfAccount
   ipGLAccount
   ds
   """  
   def __init__(self, obj):
      self.ipTypeOfAccount:str = obj["ipTypeOfAccount"]
      """  GL Account Description field  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Book account being added  """  
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class DefaultsOnAdd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BVRuleRow:
   def __init__(self, obj):
      self.BVRuleUID:int = obj["BVRuleUID"]
      """  Unique value.Primary key  """  
      self.VRuleUID:int = obj["VRuleUID"]
      """  Technical key of Validation Rule  """  
      self.Description:str = obj["Description"]
      """  Validation rule description  """  
      self.Action:str = obj["Action"]
      """  Error, Ignor, Warning, Autocorrect, Autocorrect with warning  """  
      self.VLevel:str = obj["VLevel"]
      """  Validation level : Book, Booking Rule, Company etc  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to Book.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Reference to the GL Transaction Type.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Reference to the Revision.  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicates default validation rules for ABT templates.  """  
      self.LocModified:bool = obj["LocModified"]
      """  LocModified  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ActionList:str = obj["ActionList"]
      """  List of actions (used in combo boxes).  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentNameListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountMasksRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.BookID:str = obj["BookID"]
      """  GL Book ID  """  
      self.MaskType:str = obj["MaskType"]
      """   Indicates the type of Mask to search and apply.  Valid values include:
DB = Daily Balance
RU = Roll-Up Accounts
RT = Reference Type  """  
      self.GLMaskedAccount:str = obj["GLMaskedAccount"]
      """  GL Account Mask in COA segment number format separated by the vertical bar.  This field is not intended ofr end user use.  """  
      self.GLMaskAcctDisp:str = obj["GLMaskAcctDisp"]
      """  GL Account Mask in COA display order format  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.TgtAccount:str = obj["TgtAccount"]
      """  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks.  This field is intended for internal use only.  """  
      self.TgtAcctDisp:str = obj["TgtAcctDisp"]
      """  This is the account/mask to use if the mask matches the transactional GL account.  Used with Alternative Retained Earnings Masks  """  
      self.TgtSegValue1:str = obj["TgtSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.TgtSegValue2:str = obj["TgtSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.TgtSegValue3:str = obj["TgtSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.TgtSegValue4:str = obj["TgtSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.TgtSegValue5:str = obj["TgtSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.TgtSegValue6:str = obj["TgtSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.TgtSegValue7:str = obj["TgtSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.TgtSegValue8:str = obj["TgtSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.TgtSegValue9:str = obj["TgtSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.TgtSegValue10:str = obj["TgtSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.TgtSegValue11:str = obj["TgtSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.TgtSegValue12:str = obj["TgtSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.TgtSegValue13:str = obj["TgtSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.TgtSegValue14:str = obj["TgtSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.TgtSegValue15:str = obj["TgtSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.TgtSegValue16:str = obj["TgtSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.TgtSegValue17:str = obj["TgtSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.TgtSegValue18:str = obj["TgtSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.TgtSegValue19:str = obj["TgtSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.TgtSegValue20:str = obj["TgtSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.MaskRank:int = obj["MaskRank"]
      """  Order in which Mask is applied  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
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

class Erp_Tablesets_GLBookListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.COACodeDescription:str = obj["COACodeDescription"]
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenBalUpdateOpt:str = obj["OpenBalUpdateOpt"]
      """  Indicates how opening balances will be updated  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookListTableset:
   def __init__(self, obj):
      self.GLBookList:list[Erp_Tablesets_GLBookListRow] = obj["GLBookList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBookPackageSegmentMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.Package:str = obj["Package"]
      """  Posting Rules Package  """  
      self.SourceSegmentNbr:int = obj["SourceSegmentNbr"]
      """  Segment Number in Posting Rules Package  """  
      self.TargetSegmentNbr:int = obj["TargetSegmentNbr"]
      """  Segment Number in COA of the Book  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID of the user who created the record  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date/ time that the record was created  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date/ time that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.TargetSegmentName:str = obj["TargetSegmentName"]
      """  Target Segment Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourceSegmentName:str = obj["SourceSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.COABalFmtChg:bool = obj["COABalFmtChg"]
      """  Indiates if the blaance account structure has changed on the COA.  Yes indicates it has changed and the balance rebuild utility needs to run.  This field is used internally and is not intended for end-user use.  """  
      self.REAccount:str = obj["REAccount"]
      """  Retained Earnings Account.  May be actual account or a mask  """  
      self.RESegValue1:str = obj["RESegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.RESegValue2:str = obj["RESegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.RESegValue3:str = obj["RESegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.RESegValue4:str = obj["RESegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.RESegValue5:str = obj["RESegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.RESegValue6:str = obj["RESegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.RESegValue7:str = obj["RESegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.RESegValue8:str = obj["RESegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.RESegValue9:str = obj["RESegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.RESegValue10:str = obj["RESegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.RESegValue11:str = obj["RESegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.RESegValue12:str = obj["RESegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.RESegValue13:str = obj["RESegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.RESegValue14:str = obj["RESegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.RESegValue15:str = obj["RESegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.RESegValue16:str = obj["RESegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.RESegValue17:str = obj["RESegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.RESegValue18:str = obj["RESegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.RESegValue19:str = obj["RESegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.RESegValue20:str = obj["RESegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RndTolerance:int = obj["RndTolerance"]
      """  RoundTolerance  """  
      self.RndAccount:str = obj["RndAccount"]
      """  The Account is used  in case auto balancing with rounding difference.  """  
      self.RndSegValue1:str = obj["RndSegValue1"]
      """  SegValue1 of Round Account  """  
      self.RndSegValue2:str = obj["RndSegValue2"]
      """  SegValue2 -  of Round Account  """  
      self.RndSegValue3:str = obj["RndSegValue3"]
      """  SegValue3 of RoundAccount  """  
      self.RndSegValue4:str = obj["RndSegValue4"]
      """  SegValue4 of RoundAccount  """  
      self.RndSegValue5:str = obj["RndSegValue5"]
      """  SegValue5 of RoundAccount  """  
      self.RndSegValue6:str = obj["RndSegValue6"]
      """  SegValue6 of Round Account  """  
      self.RndSegValue7:str = obj["RndSegValue7"]
      """  SegValue7 of RoundAccount  """  
      self.RndSegValue8:str = obj["RndSegValue8"]
      """  SegValue8 - of RoundAccount  """  
      self.RndSegValue9:str = obj["RndSegValue9"]
      """  SegValue9 - RoundAccount  """  
      self.RndSegValue10:str = obj["RndSegValue10"]
      """  SegValue10 - of RoundAccount  """  
      self.RndSegValue11:str = obj["RndSegValue11"]
      """  SegValue11 fo RoundAccount  """  
      self.RndSegValue12:str = obj["RndSegValue12"]
      """  SegValue12 of RoundAccount  """  
      self.RndSegValue13:str = obj["RndSegValue13"]
      """  SegValue13 of RoundAccount  """  
      self.RndSegValue14:str = obj["RndSegValue14"]
      """  SegValue14 of RoundAccount  """  
      self.RndSegValue15:str = obj["RndSegValue15"]
      """  SegValue15 of RoundAccount  """  
      self.RndSegValue16:str = obj["RndSegValue16"]
      """  SegValue16 of RoundAccount  """  
      self.RndSegValue17:str = obj["RndSegValue17"]
      """  SegValue17 of RoundAccount  """  
      self.RndSegValue18:str = obj["RndSegValue18"]
      """  SegValue18 of RoundAccount  """  
      self.RndSegValue19:str = obj["RndSegValue19"]
      """  SegValue19 of RoundAccount  """  
      self.RndSegValue20:str = obj["RndSegValue20"]
      """  SegValue20 of RoundAccount  """  
      self.CorrAccounting:bool = obj["CorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the book.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenBalUpdateOpt:str = obj["OpenBalUpdateOpt"]
      """  Indicates how opening balances will be updated  """  
      self.FromNatAccount:str = obj["FromNatAccount"]
      """  Report Default Natural Account From  """  
      self.ToNatAccount:str = obj["ToNatAccount"]
      """  Report Default Natural Account To  """  
      self.LevelList:str = obj["LevelList"]
      """  Report Default LevelList  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  DebitRateType  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  CreditRateType  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  GainAcctDesc  """  
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  LossAcctDesc  """  
      self.DefaultPackage:str = obj["DefaultPackage"]
      """  Posting Rules Package that is used by “Import GL Transaction Types” conversion program to load posting rules when there is no Revision for the GL Transaction Type being updated. Available only for Main Book.  """  
      self.EnableBookType:bool = obj["EnableBookType"]
      self.EnableCalendar:bool = obj["EnableCalendar"]
      """  Flag to indicate if the calendar id is available for input.  """  
      self.EnableCurrency:bool = obj["EnableCurrency"]
      """  Flag to indicate if the currency is available for input.  """  
      self.FiscalCalendarDesc:str = obj["FiscalCalendarDesc"]
      """  Fiscal Calendar Description  """  
      self.GLControlType:str = obj["GLControlType"]
      self.isDefaultBook:bool = obj["isDefaultBook"]
      """  The user uses this field to define the Book as Default (Main).  """  
      self.MainBookID:str = obj["MainBookID"]
      """  The BookID of the GL Book which is flagged as 'Main'.  """  
      self.REAccountDesc:str = obj["REAccountDesc"]
      """  RE Account DEscription.  """  
      self.RevalueOptDesc:str = obj["RevalueOptDesc"]
      self.RndAccoundDesc:str = obj["RndAccoundDesc"]
      self.SegmentMapIsNotRequired:bool = obj["SegmentMapIsNotRequired"]
      self.BitFlag:int = obj["BitFlag"]
      self.COACodePerBalFmt:str = obj["COACodePerBalFmt"]
      self.COACodeDescription:str = obj["COACodeDescription"]
      self.CreditRateTypeDescription:str = obj["CreditRateTypeDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DebitRateTypeDescription:str = obj["DebitRateTypeDescription"]
      self.DefaultPackagePackageName:str = obj["DefaultPackagePackageName"]
      self.RndAccountGLShortAcct:str = obj["RndAccountGLShortAcct"]
      self.RndAccountGLAcctDisp:str = obj["RndAccountGLAcctDisp"]
      self.RndAccountAccountDesc:str = obj["RndAccountAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBookTableset:
   def __init__(self, obj):
      self.GLBook:list[Erp_Tablesets_GLBookRow] = obj["GLBook"]
      self.GLBookAttch:list[Erp_Tablesets_GLBookAttchRow] = obj["GLBookAttch"]
      self.GLAccountMasks:list[Erp_Tablesets_GLAccountMasksRow] = obj["GLAccountMasks"]
      self.BVRule:list[Erp_Tablesets_BVRuleRow] = obj["BVRule"]
      self.COASegmentNameList:list[Erp_Tablesets_COASegmentNameListRow] = obj["COASegmentNameList"]
      self.MapBook:list[Erp_Tablesets_MapBookRow] = obj["MapBook"]
      self.MapACTType:list[Erp_Tablesets_MapACTTypeRow] = obj["MapACTType"]
      self.GLBookPackageSegmentMap:list[Erp_Tablesets_GLBookPackageSegmentMapRow] = obj["GLBookPackageSegmentMap"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MapACTTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LinkID:int = obj["LinkID"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      self.DisplayName:str = obj["DisplayName"]
      self.RevisionCode:str = obj["RevisionCode"]
      self.RevisionStatus:str = obj["RevisionStatus"]
      self.Limited:bool = obj["Limited"]
      self.EnableMapping:bool = obj["EnableMapping"]
      self.MapExists:bool = obj["MapExists"]
      self.TrgBook:str = obj["TrgBook"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MapBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LinkID:int = obj["LinkID"]
      """  LinkID  """  
      self.TrgBook:str = obj["TrgBook"]
      """  TrgBook  """  
      self.SrcBook:str = obj["SrcBook"]
      """  SrcBook  """  
      self.TranCurr:int = obj["TranCurr"]
      """  TranCurr  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  COAMapUID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SrcBookCOA:str = obj["SrcBookCOA"]
      """  Source Book COA  """  
      self.TrgBookCOA:str = obj["TrgBookCOA"]
      """  Target Book COA  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtGLBookTableset:
   def __init__(self, obj):
      self.GLBook:list[Erp_Tablesets_GLBookRow] = obj["GLBook"]
      self.GLBookAttch:list[Erp_Tablesets_GLBookAttchRow] = obj["GLBookAttch"]
      self.GLAccountMasks:list[Erp_Tablesets_GLAccountMasksRow] = obj["GLAccountMasks"]
      self.BVRule:list[Erp_Tablesets_BVRuleRow] = obj["BVRule"]
      self.COASegmentNameList:list[Erp_Tablesets_COASegmentNameListRow] = obj["COASegmentNameList"]
      self.MapBook:list[Erp_Tablesets_MapBookRow] = obj["MapBook"]
      self.MapACTType:list[Erp_Tablesets_MapACTTypeRow] = obj["MapACTType"]
      self.GLBookPackageSegmentMap:list[Erp_Tablesets_GLBookPackageSegmentMapRow] = obj["GLBookPackageSegmentMap"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FillACTTypes_input:
   """ Required : 
   trgBook
   srcBook
   linkID
   ds
   """  
   def __init__(self, obj):
      self.trgBook:str = obj["trgBook"]
      """  Target Book  """  
      self.srcBook:str = obj["srcBook"]
      """  Source Book  """  
      self.linkID:int = obj["linkID"]
      """  linkID  """  
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class FillACTTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class FillDataForSrcBook_input:
   """ Required : 
   srcBookID
   ds
   """  
   def __init__(self, obj):
      self.srcBookID:str = obj["srcBookID"]
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class FillDataForSrcBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAccountDescription_input:
   """ Required : 
   ipCOACode
   ipAccount
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COACode  """  
      self.ipAccount:str = obj["ipAccount"]
      """  GL Account  """  
      pass

class GetAccountDescription_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Account Description  """  
      pass

class GetByID_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBookTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBookTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBookTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  table name  """  
      self.fieldName:str = obj["fieldName"]
      """  field name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListManual_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Query-like string  """  
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
      self.returnObj:list[Erp_Tablesets_GLBookListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBVRule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class GetNewBVRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOASegmentNameList_input:
   """ Required : 
   ds
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewCOASegmentNameList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLAccountMasks_input:
   """ Required : 
   ds
   coACode
   bookID
   maskType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.bookID:str = obj["bookID"]
      self.maskType:str = obj["maskType"]
      pass

class GetNewGLAccountMasks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBookAttch_input:
   """ Required : 
   ds
   bookID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      pass

class GetNewGLBookAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBookPackageSegmentMap_input:
   """ Required : 
   ds
   bookID
   package
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.package:str = obj["package"]
      pass

class GetNewGLBookPackageSegmentMap_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBook_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class GetNewGLBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLinkWithID_input:
   """ Required : 
   trgBook
   ds
   """  
   def __init__(self, obj):
      self.trgBook:str = obj["trgBook"]
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class GetNewLinkWithID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLink_input:
   """ Required : 
   trgBook
   linkID
   ds
   """  
   def __init__(self, obj):
      self.trgBook:str = obj["trgBook"]
      """  Target Book  """  
      self.linkID:int = obj["linkID"]
      """  linkID  """  
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class GetNewLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMapBook_input:
   """ Required : 
   ds
   linkID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      self.linkID:int = obj["linkID"]
      pass

class GetNewMapBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBook
   whereClauseGLBookAttch
   whereClauseGLAccountMasks
   whereClauseBVRule
   whereClauseCOASegmentNameList
   whereClauseMapBook
   whereClauseMapACTType
   whereClauseGLBookPackageSegmentMap
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBook:str = obj["whereClauseGLBook"]
      self.whereClauseGLBookAttch:str = obj["whereClauseGLBookAttch"]
      self.whereClauseGLAccountMasks:str = obj["whereClauseGLAccountMasks"]
      self.whereClauseBVRule:str = obj["whereClauseBVRule"]
      self.whereClauseCOASegmentNameList:str = obj["whereClauseCOASegmentNameList"]
      self.whereClauseMapBook:str = obj["whereClauseMapBook"]
      self.whereClauseMapACTType:str = obj["whereClauseMapACTType"]
      self.whereClauseGLBookPackageSegmentMap:str = obj["whereClauseGLBookPackageSegmentMap"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBookTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

class IsBalanceSegmentUpdated_input:
   """ Required : 
   segmentName
   ipCOACodePerBalFmt
   """  
   def __init__(self, obj):
      self.segmentName:str = obj["segmentName"]
      self.ipCOACodePerBalFmt:str = obj["ipCOACodePerBalFmt"]
      pass

class IsBalanceSegmentUpdated_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class MaskValidate_input:
   """ Required : 
   tableName
   glAccount
   mask
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table name the tested account belongs to  """  
      self.glAccount:str = obj["glAccount"]
      """  GL account  """  
      self.mask:str = obj["mask"]
      """  Mask symbol '_' or '%'  """  
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class MaskValidate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MultiCurrencyChecksLicensed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeCurrencyCode_input:
   """ Required : 
   ipCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  The Currency Code entered  """  
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class OnChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RetrieveACTTypesToReview_input:
   """ Required : 
   bookID
   packageList
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  Book ID where segment map has changed.  """  
      self.packageList:str = obj["packageList"]
      """  List delimited packages where segment map has changed.  """  
      pass

class RetrieveACTTypesToReview_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of ACTTypes.  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBookTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBookTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateTransactionTypes_input:
   """ Required : 
   ipTrgBook
   ipSrcBook
   ipCOAMapUID
   ipTranCurr
   ds
   """  
   def __init__(self, obj):
      self.ipTrgBook:str = obj["ipTrgBook"]
      self.ipSrcBook:str = obj["ipSrcBook"]
      self.ipCOAMapUID:int = obj["ipCOAMapUID"]
      self.ipTranCurr:int = obj["ipTranCurr"]
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class UpdateTransactionTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidAccount_input:
   """ Required : 
   coaCode
   segmentCode
   restrictID
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      self.segmentCode:str = obj["segmentCode"]
      self.restrictID:str = obj["restrictID"]
      pass

class ValidAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidGLAccount_input:
   """ Required : 
   glAccount
   ipCoaCode
   reActFlag
   """  
   def __init__(self, obj):
      self.glAccount:str = obj["glAccount"]
      self.ipCoaCode:str = obj["ipCoaCode"]
      self.reActFlag:bool = obj["reActFlag"]
      pass

class ValidGLAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.REAccountDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateStdAccount_input:
   """ Required : 
   ipCOACode
   ipGLAccount
   ipSegValue1
   ipSegValue2
   ipSegValue3
   ipSegValue4
   ipSegValue5
   ipSegValue6
   ipSegValue7
   ipSegValue8
   ipSegValue9
   ipSegValue10
   ipSegValue11
   ipSegValue12
   ipSegValue13
   ipSegValue14
   ipSegValue15
   ipSegValue16
   ipSegValue17
   ipSegValue18
   ipSegValue19
   ipSegValue20
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipGLAccount:str = obj["ipGLAccount"]
      self.ipSegValue1:str = obj["ipSegValue1"]
      self.ipSegValue2:str = obj["ipSegValue2"]
      self.ipSegValue3:str = obj["ipSegValue3"]
      self.ipSegValue4:str = obj["ipSegValue4"]
      self.ipSegValue5:str = obj["ipSegValue5"]
      self.ipSegValue6:str = obj["ipSegValue6"]
      self.ipSegValue7:str = obj["ipSegValue7"]
      self.ipSegValue8:str = obj["ipSegValue8"]
      self.ipSegValue9:str = obj["ipSegValue9"]
      self.ipSegValue10:str = obj["ipSegValue10"]
      self.ipSegValue11:str = obj["ipSegValue11"]
      self.ipSegValue12:str = obj["ipSegValue12"]
      self.ipSegValue13:str = obj["ipSegValue13"]
      self.ipSegValue14:str = obj["ipSegValue14"]
      self.ipSegValue15:str = obj["ipSegValue15"]
      self.ipSegValue16:str = obj["ipSegValue16"]
      self.ipSegValue17:str = obj["ipSegValue17"]
      self.ipSegValue18:str = obj["ipSegValue18"]
      self.ipSegValue19:str = obj["ipSegValue19"]
      self.ipSegValue20:str = obj["ipSegValue20"]
      pass

class ValidateStdAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.upDescription:str = obj["parameters"]
      self.upWarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class WriteChgLog_input:
   """ Required : 
   actTypeUID
   oldRevUID
   newRevUID
   """  
   def __init__(self, obj):
      self.actTypeUID:int = obj["actTypeUID"]
      """  ACTType UID  """  
      self.oldRevUID:int = obj["oldRevUID"]
      """  Old Revision  """  
      self.newRevUID:int = obj["newRevUID"]
      """  New revision  """  
      pass

class WriteChgLog_output:
   def __init__(self, obj):
      pass

